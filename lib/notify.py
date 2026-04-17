"""Gmail SMTP helper for career-ops digest emails."""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject: str, body: str, to: str = "shivamsharma2023@gmail.com") -> None:
    user = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to
    msg.attach(MIMEText(body, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(user, password)
        server.sendmail(user, [to], msg.as_string())
