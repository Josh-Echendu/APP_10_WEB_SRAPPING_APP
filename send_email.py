import smtplib, ssl

def email1(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "echendujosh@gmail.com"
    password = "lucw pxji csbq ppqm"

    reciever = "joshanu55@gmail.com"
    context = ssl.create_default_context() #we created a secure context using the SSL library

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, reciever, message)

    print('Email was sent')    


