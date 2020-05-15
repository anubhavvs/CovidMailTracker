import smtplib

def sendemails(sender,reciever, password, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(sender, password)
    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail('Virus Alert', reciever, msg)

    print('Mail has been sent')
    server.quit()