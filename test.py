import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send():
    port = 465
    password = 'Amu2020@'
    email = 'krashant76@gmail.com'
    context = ssl.create_default_context()

    sender_email = email
    receiver_email = "divyanksingh20@gmail.com"

    message = f"""\
        Name : 0
        Date : 0
        Time : 0
        Disease : 0
        Doctor : 0
        """
    print(message)

    msg=MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Appointment booked"
    msg.attach(MIMEText(message,'plain'))

    session = smtplib.SMTP('smtp.gmail.com', port)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = msg.as_string()
    session.sendmail(sender_email,receiver_email, text)
    session.quit()
    print("success")

send()