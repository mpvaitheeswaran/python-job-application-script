import smtplib
import csv
from email.message import EmailMessage

import os
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

print("EMAIL:", EMAIL)
print("PASSWORD:", PASSWORD)

if not EMAIL:
    raise ValueError("EMAIL environment variable not set")

if not PASSWORD:
    raise ValueError("EMAIL_APP_PASSWORD environment variable not set")


# Load subject
with open("subject.txt") as f:
    SUBJECT = f.read().strip()

# Load HTML template
with open("email_template.html") as f:
    HTML_TEMPLATE = f.read()

with open("recipients.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = row["email"]
        msg["Subject"] = SUBJECT

        # Set HTML content
        msg.add_alternative(
            HTML_TEMPLATE.format(
                name=row["name"],
                company=row["company"]
            ),
            subtype="html"
        )

        # Attach resume
        with open("resume.pdf", "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename="Vaitheeswaran_Resume.pdf"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)

print("All emails sent successfully!")
