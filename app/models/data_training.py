from app.extensions import db

class Data_Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    X1 = db.Column(db.Float, nullable=False)
    X2 = db.Column(db.Float, nullable=False)
    X3 = db.Column(db.Float, nullable=False)
    X4 = db.Column(db.Float, nullable=False)
    X5 = db.Column(db.Float, nullable=False)
    X6 = db.Column(db.Float, nullable=False)
    Y = db.Column(db.Float, nullable=False)