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
    return jsonify({"message": "The payment has been confirmed"})

@bp.route('/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = PaymentService.get_payment(payment_id)
    return render_template('payment.html', payment_id = payment.id, value = payment.value, host = 'http://127.0.0.1:5000', qr_code = payment.qr_code)
