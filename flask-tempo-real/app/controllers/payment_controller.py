from flask import Blueprint, request, jsonify
from app.services.payment_service import PaymentService
from datetime import datetime, timedelta

bp = Blueprint('payment', __name__, url_prefix='/payments')

@bp.route('/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()

    if not 'value' in data:
        return jsonify({"message": "Invalid value"}), 400
    
    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = PaymentService.create_payment(value=data['value'], expiration_date=expiration_date)

    return jsonify({"message": "The payment has been created", "payment": new_payment.to_dict()})

@bp.route('/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed"})

@bp.route('/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'pagamento PIX'
