from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt, os
from .otp import create_and_send_otp, verify_otp_code

router = APIRouter()
SECRET = os.getenv("SECRET_KEY", "change-me")

class OTPRequest(BaseModel):
    email: str

class OTPVerify(BaseModel):
    email: str
    code: str

@router.post("/request-otp")
def request_otp(payload: OTPRequest):
    create_and_send_otp(payload.email)
    return {"msg": "OTP sent"}

@router.post("/verify-otp")
def verify_otp(payload: OTPVerify):
    ok = verify_otp_code(payload.email, payload.code)
    if not ok:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")
    token = jwt.encode({"sub": payload.email, "exp": datetime.utcnow() + timedelta(hours=8)}, SECRET, algorithm="HS256")
    return {"access_token": token}
