import sys
sys.path.append('../')

import pytest
import os
from app.payments.pix import Pix

def test_pix_create_payment():
  pix_instance = Pix()

  payment_info = pix_instance.create_payment()
  
  assert "qr_code_path" in payment_info
  assert "bank_payment_id" in payment_info

  qr_code_path = payment_info["qr_code_path"]
  assert os.path.isfile(f"../app/static/img/{qr_code_path}.png")
