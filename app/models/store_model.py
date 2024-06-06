from app.database import db

class Store(db.Model):
    ___tablename__="producto"
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    stock = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, description, price, stock):
        self.name=name
        self.description=description
        self.price=float(price)
        self.stock=stock
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Store.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Store.query.get(id)
        
    def update(self, name=None, description=None, price=None, stock=None):
        if name is not None:
            self.name=name
        if description is not None:
            self.description=description
        if price is not None:
            self.price=price
        if stock is not None:
            self.stock=stock
        db.session.commit()
        
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        