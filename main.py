from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from email.mime.text import MIMEText
import smtplib
import os

app = FastAPI()



EMAIL = "resend"
PASSWORD = "re_hZKpYLqw_Lsryq8wCqqpx3PxujeGHuHDq"


def email_que(email: str):
    try:
        msg_temp = """
        <html>
            <body>
                <h1>Welcome!</h1>
                <p>Your account has been created successfully.</p>
            </body>
        </html>
        """

        msg = MIMEText(msg_temp, "html")
        msg["Subject"] = "Welcome message from API"
        msg["From"] = f"Nithish <{EMAIL}>"
        msg["To"] = email

        server = smtplib.SMTP_SSL(
            "smtp.resend.com",
            465 
        )

        server.login(EMAIL, PASSWORD)

        server.sendmail(
            EMAIL,
            email,
            msg.as_string()
        )

        server.quit()

        print(f"Email sent to {email}")

    except Exception as e:
        print("EMAIL ERROR:", str(e))


@app.post("/send-mail")
def send_mail(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        email_que,
        email
    )

    return {
        "message": "Email queued successfully"
    }
