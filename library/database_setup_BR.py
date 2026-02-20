from flask import Flask
from models import db, BookRequest
from werkzeug.security import generate_password_hash
def setup_database():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()
        
if __name__ == '__main__':
    setup_database()
