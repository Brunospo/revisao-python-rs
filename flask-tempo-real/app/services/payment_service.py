from app.models.payment import Payment
from app.extensions import db

class PaymentService:
    @staticmethod
    def get_all_payments():
        return Payment.query.all()

    @staticmethod
    def create_payment(value, expiration_date):
        payment = Payment(value=value, expiration_date=expiration_date)
        db.session.add(payment)
        db.session.commit()
        return payment
