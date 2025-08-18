from app.models.payment import Payment
from app.extensions import db
from datetime import datetime, timedelta
from app.payments.pix import Pix

class PaymentService:
    @staticmethod
    def get_payment(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def create_payment(value):
        pix_data = Pix.create_payment() # Chama o Pix para simular a criação do pagamento na instituição financeira

        expiration_date = datetime.now() + timedelta(minutes=30)
        bank_payment_id = pix_data.get('bank_payment_id')
        qr_code_path = pix_data.get('qr_code_path')

        payment = Payment(value=value, expiration_date=expiration_date, bank_payment_id=bank_payment_id, qr_code=qr_code_path)
        db.session.add(payment)
        db.session.commit()
        return payment
