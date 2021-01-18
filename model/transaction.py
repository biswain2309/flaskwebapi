from app import db

class Transaction(db.Model):
        creditCardNumber = db.Column(db.String, unique=True)
        cardHolder = db.Column(db.String, unique=True)
        expirationDate = expirationDate
        securityCode = securityCode
        amount = amount
