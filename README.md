#  Automated Job Application Email Sender (Python)

This tool automates sending job application emails with resume attachments to multiple recipients using Gmail SMTP.  
It supports **configurable subject**, **HTML email templates**, **environment variables**, and **Gmail 2FA (App Password)**.

---

##  Features
- Send emails to multiple recipients automatically
- Configurable email subject (no code change required)
- HTML email template with clickable links
- Resume attachment support
- Gmail 2FA support using App Password
- Easy recipient management using CSV file
- Secure credential handling via environment variables

---

##  Project Structure
```
python-job-application-script/
│── send_email.py
│── recipients.csv
│── subject.txt
│── email_template.html
│── resume.pdf
│── README.md
```


---

## 🛠 Prerequisites
- Python **3.9+**
- Gmail account with **2-Step Verification enabled**
- Gmail **App Password**
- Internet connection

---

##  Gmail App Password Setup (Required)

> Do NOT use your Gmail login password.

1. Go to **Google Account → Security**
2. Enable **2-Step Verification**
3. Click **App passwords**
4. Select:
   - App: `Mail`
   - Device: `Other`
5. Generate the password
6. Copy the **16-character App Password**

---

## Environment Variable Setup

###  Windows (Permanent – Recommended)

1. Open **Start Menu**
2. Search **Edit the system environment variables**
3. Click **Environment Variables**
4. Under **User variables**, click **New**

Add the following variables:

| Variable Name | Value |
|--------------|-------|
| `EMAIL` | yourgmail@gmail.com |
| `EMAIL_APP_PASSWORD` | your_16_char_app_password |

5. Click **OK** → **OK**
6. Restart **Command Prompt / VS Code / Terminal**

###  Windows (Using CMD)

```bat
set EMAIL=yourgmail@gmail.com
set EMAIL_APP_PASSWORD=your_16_char_app_password
```

#### Verify:
```bat
echo %EMAIL%
echo %EMAIL_APP_PASSWORD%
```

#### Run the Code:

```bat
python send_email.py
```