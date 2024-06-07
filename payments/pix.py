import uuid
import qrcode

class Pix:
  def __init__(self):
    pass
  
  def create_payment(self, base_dir=""):
    
    #criar o pagamento na instituição financeira
    bank_payment_id = str(uuid.uuid4())
    
    #codigo_copia e cola
    hash_payment = f'hash_payment_{bank_payment_id}'
    
    #qr code
    img = qrcode.make(hash_payment)
    
    #salvar o qr code como arquivo PNG
    img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")
    
    return {"bank_payments": bank_payment_id,
            "qr_code": f"qr_code_payment_{bank_payment_id}"}