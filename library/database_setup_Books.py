from flask import Flask
from models import db, Book
# from werkzeug.security import generate_password_hash
def setup_database():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

        book1 = Book(
            title='プログラミングの基礎', 
            author='Taro Yamada', 
            isbn='978-4000000010',
        )

        book2 = Book(
            title='Webデザイン入門',
            author='Jiro Tanaka',
            isbn='978-4000000027',
            )

        book3 = Book(
            title='図書館の歴史', 
            author='Saburo Sato', 
            isbn='978-4000000034',
        )

        book4 = Book(
            title='Flaskでデモアプリ', 
            author='Hanako Ito', 
            isbn='978-4000000041'
        )

        db.session.add_all([book1, book2, book3, book4])
        db.session.commit()
        
if __name__ == '__main__':
    setup_database()
