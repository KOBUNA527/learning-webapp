from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap5
from sqlalchemy import or_
from forms import LoginForm, BookRequestForm, SearchForm
from werkzeug.security import check_password_hash
from models import db, User, BookRequest, Book, Loan

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY_FOR_DEVELOPMENT"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Bootstrap5(app)
db.init_app(app)
@app.route("/login", methods=["GET", "POST"])
def login():
    user_id = session.get("user_id")
    if user_id:
        return redirect(url_for("index"))   
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            session["user_id"] = user.id            
            flash("ログインに成功しました", "success")
            return redirect(url_for("index"))
        else:
            flash("ユーザーIDまたはパスワードが間違っています", "danger")
    return render_template("login.html", form=form)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("ログアウトしました", "success")
    return redirect(url_for("login"))

request_list_data = []
@app.route("/request_book", methods=["GET", "POST"])
def request_book():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)

    form = BookRequestForm()

    if form.validate_on_submit():
        book_request = BookRequest(
            title=form.title.data,
            author=form.author.data,
            reason=form.reason.data,
        )
        db.session.add(book_request)
        db.session.commit()
        return redirect(url_for("request_list"))
    return render_template(
        "request_form.html", form=form, username=current_user.username
    )

@app.route("/search", methods=["GET", "POST"])
def search():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)

    form = SearchForm()
    books = []

    if form.validate_on_submit():
        search_term = form.search_term.data
        search_pattern = f"%{search_term}%"
        books = Book.query.filter(
            or_(Book.title.like(search_pattern), Book.author.like(search_pattern))
        ).all()

        if not books:
            flash(f"「{search_term}」に一致する書籍は見つかりませんでした","info")
    return render_template(
        "search.html", form=form, books= books, username=current_user.username
    )


@app.route("/request_list")
def request_list():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)
    book_requests = BookRequest.query.all()
    return render_template(
        "request_list.html", requests = book_requests, username = current_user.username
    )

@app.route('/')
def index():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)

    today = datetime.now().strftime("%Y年%m月%d日")
    return_deadline = (datetime.now() + timedelta(weeks=2)).strftime("%Y年%m月%d日")
    return render_template(
        "index.html",
        today=today,
        return_deadline=return_deadline,
        username = current_user.username
        )

@app.route("/borrow/<int:book_id>", methods=["POST"])
def borrow(book_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("index"))
    current_user = User.query.get(user_id)

    book = Book.query.get_or_404(book_id)

    if book.is_borrowed:
        flash("この書籍はすでに貸出中です", "warning")
        return redirect(url_for("search"))

    loan = Loan(user=current_user, book=book)
    db.session.add(loan)
    db.session.commit()

    flash(f"「{book.title}」を借りました", "success")
    return redirect(url_for("search"))

@app.route("/borrowed_books")
def borrowed_books():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)
    borrowed_list = Loan.query.filter_by(user=current_user, returned_at=None).all()

    return render_template(
        "borrowed_books.html", borrowed_list=borrowed_list, username=current_user.username
    )

@app.route("/return_book/<int:loan_id>", methods=["POST"])
def return_book(loan_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)

    loan = Loan.query.filter_by(
        id=loan_id, user=current_user, returned_at=None
    ).first_or_404()
    if not loan:
        flash("返却できる貸出情報が見つかりません", "warning")
        return redirect(url_for("search"))
    loan.returned_at = db.func.now()
    db.session.commit()

    flash("返却しました", "success")
    return redirect(url_for("borrowed_books"))

@app.route("/extend_book/<int:loan_id>", methods=["POST"])
def extend_book(loan_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)

    loan = Loan.query.filter_by(
        id=loan_id, user=current_user,
    ).first_or_404()
    # if not loan:
    #     flash("返却できる貸出情報が見つかりません", "warning")
    #     return redirect(url_for("search"))
    diffdate = loan.due_date - loan.borrowed_at

    if diffdate.days < 60:
        loan.due_date += timedelta(days=14)
        db.session.commit()
        flash("返却日を延長しました", "success")
        return redirect(url_for("borrowed_books"))
    else:
        flash("これ以上延長できません", "warning")
        return redirect(url_for("borrowed_books"))

# このファイルが直接実行された場合にサーバーを起動
if __name__ == '__main__':
    # debug=Trueにすると、コードを変更したときに自動で再起動される
    app.run(debug=True)

