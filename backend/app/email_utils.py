import os
try:
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
except Exception:
    SendGridAPIClient = None
    Mail = None

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM", "noreply@yourdomain.com")

def send_email(to: str, subject: str, body: str):
    if not SENDGRID_API_KEY or SendGridAPIClient is None:
        print("SENDGRID not configured. Email content:\n", subject, body)
        return None
    message = Mail(from_email=EMAIL_FROM, to_emails=to, subject=subject, html_content=body)
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    return response.status_code
