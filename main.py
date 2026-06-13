from email.mime.text import MIMEText
import smtplib
from fastapi import FastAPI, Depends, HTTPException , BackgroundTasks
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import socket


app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def email_que(email: str):

    EMAIL = "nithishanaricle@gmail.com"
    PASSWORD = "oumw plqm vpnb kreo" 

        # SMTP setup
    server = smtplib.SMTP("smtp.gmail.com", 465)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    msg_temp = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Welcome Email</title>
</head>
<body style="margin:0;padding:0;background-color:#f4f7fc;font-family:Arial,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f4f7fc">
    <tr>
        <td align="center" style="padding:40px 20px;">

            <!-- Container -->
            <table width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="border-radius:12px;overflow:hidden;">

                <!-- Header -->
                <tr>
                    <td align="center" bgcolor="#2563eb" style="padding:40px 20px;">
                        <h1 style="margin:0;color:#ffffff;font-size:32px;">
                            Welcome!
                        </h1>
                        <p style="margin:10px 0 0;color:#dbeafe;font-size:16px;">
                            We're excited to have you here.
                        </p>
                    </td>
                </tr>

                <!-- Content -->
                <tr>
                    <td style="padding:40px 35px;">

                        <h2 style="margin-top:0;color:#1f2937;">
                            Hello {{name}},
                        </h2>

                        <p style="color:#4b5563;font-size:16px;line-height:1.7;">
                            Thank you for joining <strong>Your Company Name</strong>.
                            We're thrilled to welcome you to our community.
                        </p>

                        <p style="color:#4b5563;font-size:16px;line-height:1.7;">
                            Your account has been successfully created, and you're ready to explore everything we have to offer.
                        </p>

                        <!-- CTA Button -->
                        <table cellpadding="0" cellspacing="0" border="0" align="center" style="margin:30px auto;">
                            <tr>
                                <td bgcolor="#2563eb" style="border-radius:6px;">
                                    <a href="https://yourwebsite.com"
                                       style="display:inline-block;padding:14px 28px;color:#ffffff;text-decoration:none;font-size:16px;font-weight:bold;">
                                        Get Started
                                    </a>
                                </td>
                            </tr>
                        </table>

                        <p style="color:#4b5563;font-size:16px;line-height:1.7;">
                            If you have any questions, simply reply to this email. We're always happy to help.
                        </p>

                        <p style="color:#1f2937;font-size:16px;">
                            Best regards,<br>
                            <strong>The Your Company Team</strong>
                        </p>

                    </td>
                </tr>

                <!-- Footer -->
                <tr>
                    <td align="center" bgcolor="#f8fafc" style="padding:25px;color:#6b7280;font-size:13px;">
                        © 2026 Your Company Name. All rights reserved.<br>
                        Your Company Address
                    </td>
                </tr>

            </table>

        </td>
    </tr>
</table>

</body>
</html>'''
    msg = MIMEText(msg_temp , "html")
    msg["Subject"] = "Welcome message from api"
    msg["From"] = "Nithish <nithishanaricle@gmail.com>"
    msg["To"] = email
    server.sendmail(EMAIL, email, msg.as_string())
    server.quit()


@app.post("/send-mail")
def send_mail(background_tasks: BackgroundTasks, email: str):
    print("Resolving...")
    print(socket.gethostbyname("smtp.gmail.com"))

    print("Connecting...")
    server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
    background_tasks.add_task(email_que, email)
    return {"message": "Email is being sent in the background."}
