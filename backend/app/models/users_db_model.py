from ..utils import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<User {self.fullname}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
