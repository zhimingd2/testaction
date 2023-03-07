import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def main( filename ):
    print(filename[0])
    sender_email = "shptxc@gmail.com"
    receiver_email = "zhiming.dai.bill@gmail.com"
    password = "uwawypwbcuxfcnbp"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Header('Test Action', 'utf-8').encode()

    if( filename[0] is not None ):
        f = open(filename[0], "r")
        body = f.read()
    else:
        body = 'Hello ! no message'

    msg_content = MIMEText(body, 'plain', 'utf-8')
    msg.attach(msg_content)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])