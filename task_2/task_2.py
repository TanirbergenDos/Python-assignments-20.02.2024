import smtplib
from email.message import EmailMessage

# Determine your email
EMAIL_FROM = "your_email"
# Define the APP password (better to reference externally)
PASSWORD = "your_app_password"


def send_mail_with_excel(recipient_email, subject, content, excel_file):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = recipient_email
    msg.set_content(content)

    with open(excel_file, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename='Tcspykjsni2024-02-20261.xlsx')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_FROM, PASSWORD)
        smtp.send_message(msg)


def main():
    directory = r"..\task_1\мои документы\skcu\Tcspykjsni2024-02-20261.xlsx"

    # Determine recipient's email
    email_to = "recipient's_email"

    subject = "Excel file from the first task"  
    send_mail_with_excel(email_to, subject, "File:", directory)


if __name__ == "__main__":
    main()
