import smtplib
import ssl


def mail_notifier(remail, jid):
    try:
        """Stuurt een email notificatie mnaar de gebruiker zodra de blast klaar is.
        """
        port = 465
        email = "1a3blastapp@gmail.com"
        password = "3-gj56QJc'5{"

        context = ssl.create_default_context()

        message = """
        Blast job voltooid! De resultaten zijn te vinden op: 
        app.opusflights.com/blastuser.html met job ID: {}
        
        
        """.format(str(jid))

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email, password)
            server.sendmail(email, str(remail), message)
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")
