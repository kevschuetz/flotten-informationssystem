from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from main import db, login_manager


@login_manager.user_loader
def load_user(user_email):
    return User.query.get(user_email)


class User(UserMixin,db.Model):
    __tablename__='users'

    email = db.Column(db.String(120), primary_key=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def get_id(self):
        return self.email

class Waggon(db.Model):
    fahrgestellnummer = db.Column(db.String(64), primary_key=True)
    spurweite = db.Column(db.Integer, index=True)
    is_available = db.Column(db.Boolean, default=True)
    __abstract__ = True

    def __repr__(self):
        return 'Triebwagen {}'.format(self.fahrgestellnummer)


class Triebwagen(Waggon):
    zugkraft = db.Column(db.DECIMAL)

class Personenwaggon(Waggon):
    sitzanzahl = db.Column(db.Integer)
    maxGewicht = db.Column(db.DECIMAL)





