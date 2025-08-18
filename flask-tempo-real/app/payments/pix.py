# simulando dados recebidos de uma instituição de pagamento

import uuid
import qrcode
import os

class Pix:
  def __init__(self):
    pass

  @staticmethod
  def create_payment():
    # criar um pagamento na instituição financeira
    bank_payment_id = str(uuid.uuid4())

    # codigo copia e cola
    hash_payment = f'hash_payment_{bank_payment_id}'

    # Caminho absoluto para static/img dentro do app
    img_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'img')
    img_dir = os.path.abspath(img_dir)

    # Garante que a pasta exista
    os.makedirs(img_dir, exist_ok=True)

    # Salva o QR Code
    img_path = os.path.join(img_dir, f'qr_code_payment_{hash_payment}.png')

    # qr code
    img = qrcode.make(hash_payment)
    # img.save(f'./static/img/qr_code_payment_{hash_payment}.png')
    img.save(img_path)

    return {
      "bank_payment_id": bank_payment_id,
      "qr_code_path": f"qr_code_payment_{hash_payment}"
    }