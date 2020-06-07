import smtplib, ssl


def mail_notifier(remail, jid):
    port = 465
    email = "1a3blastapp@gmail.com"
    password = "3-gj56QJc'5{"

    context = ssl.create_default_context()

    message = """
    Blast job completed! View the results at: app.opusflights.com/blastuser.html with job ID: {}
    
    
    """.format(str(jid))

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, str(remail), message)

    print("MAIL SENT")