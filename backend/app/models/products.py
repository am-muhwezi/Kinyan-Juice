from ..utils import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(40))
    price=db.Column(db.Float)
    description=db.Column(db.String(100))


    def __repr__(self):
        return f"<Order {self.name}>"


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    