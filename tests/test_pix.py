import sys 
sys.path.append("../")

import pytest
import os
from payments.pix import Pix


def test_pix_create_payment():
  pix_instance = Pix()
  
  #criar o pagamento na instituição financeira  
  payment_info = pix_instance.create_payment(base_dir="../")
  
  assert "bank_payments" in payment_info
  assert "qr_code" in payment_info
  
  qr_code = payment_info["qr_code"]
  assert os.path.isfile(f"../static/img/{qr_code}.png")
