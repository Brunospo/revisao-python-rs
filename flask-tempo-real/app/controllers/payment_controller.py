from flask import Blueprint, request, jsonify, send_file, render_template
from app.services.payment_service import PaymentService
import os

bp = Blueprint('payment', __name__, url_prefix='/payments')

@bp.route('/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()

    if not 'value' in data:
        return jsonify({"message": "Invalid value"}), 400

    new_payment = PaymentService.create_payment(value=data['value'])

    return jsonify({"message": "The payment has been created", "payment": new_payment.to_dict()})

@bp.route('/pix/qr_code/<file_name>', methods=['GET'])
def get_image(file_name):
    current_dir = os.getcwd()
    img_dir = os.path.join(current_dir, 'app', 'static', 'img')
    return send_file(f'{img_dir}/{file_name}.png', mimetype='image/png')

@bp.route('/pix/confirmation', methods=['POST'])
def pix_confirmation():
    data = request.get_json()

    if "bank_payment_id" not in data and "value" not in data:
        return jsonify({"message": "Invalid payment data"}), 400
    
    payment = PaymentService.get_by_bank_payment_id(data.get('bank_payment_id'))

    if not payment:
        return jsonify({"message": "Payment not found"}),404
    
    if data.get('value') != payment.value:
        return jsonify({"message": "Invalid payment data"}),400
    
    try:
        PaymentService.confirm_payment(payment)
        return jsonify({"message": "The payment has been confirmed"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@bp.route('/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = PaymentService.get_payment(payment_id)

    if not payment:
        return render_template('404.html')
    
    if payment.paid:
        return render_template('confirmed_payment.html', payment_id = payment.id, value = payment.value)
    return render_template('payment.html', payment_id = payment.id, value = payment.value, host = 'http://127.0.0.1:5000', qr_code = payment.qr_code)
