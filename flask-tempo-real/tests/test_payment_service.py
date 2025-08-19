import pytest
from app.services.payment_service import PaymentService
from app.models.payment import Payment
from datetime import datetime, timedelta

def test_create_payment(app):
  with app.app_context():
    payment = PaymentService.create_payment(100.0)

    assert payment.id is not None
    assert payment.value == 100.0
    assert isinstance(payment.expiration_date, datetime)
    assert payment.paid is False

def test_confirm_payment(app):
  with app.app_context():
    payment = PaymentService.create_payment(50.0)
    PaymentService.confirm_payment(payment)

    assert payment.paid is True

def test_cannot_confirm_expired_payment(app):
  with app.app_context():
    payment = PaymentService.create_payment(200.0)
    payment.expiration_date = datetime.now() - timedelta(minutes=1)

    with pytest.raises(ValueError, match="Payment expired"):
      PaymentService.confirm_payment(payment)
