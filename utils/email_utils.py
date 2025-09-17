import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "ds6094168@gmail.com"  # Replace with your email
SMTP_PASS = "cvht ouhr lzfg vguc"    # Replace with your app password
ADMIN_EMAIL = "sathish.deivasigamani@workiy.ca"

def send_email(to_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, to_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        

def send_email_admin( subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = ADMIN_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, ADMIN_EMAIL, msg.as_string())
        server.quit()
        print("✅ Admin Email sent successfully")
    except Exception as e:
        print(f"❌ Error sending email: {e}")