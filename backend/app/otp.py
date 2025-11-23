from datetime import datetime, timedelta
from .database import SessionLocal
from .models import OTP
import random
from .email_utils import send_email

def generate_code():
    return "%06d" % random.randint(0, 999999)

def create_and_send_otp(email: str):
    db = SessionLocal()
    code = generate_code()
    expires = datetime.utcnow() + timedelta(minutes=10)
    ot = OTP(email=email, code=code, expires_at=expires)
    db.add(ot); db.commit(); db.close()
    send_email(to=email, subject="Your OTP", body=f"Your OTP is {code}. Expires in 10 minutes.")

def verify_otp_code(email: str, code: str):
    db = SessionLocal()
    ot = db.query(OTP).filter_by(email=email, code=code, used=False).order_by(OTP.expires_at.desc()).first()
    if not ot:
        return False
    if ot.expires_at < datetime.utcnow():
        return False
    ot.used = True
    db.commit(); db.close()
    return True
