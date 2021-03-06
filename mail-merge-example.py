import csv, smtplib
port = 465 
smtp_server = "smtp.googlemail.com"
login = "john.howell.test@gmail.com" # paste your login generated by Mailtrap
password = "H8mJgqPM.X" # paste your password generated by Mailtrap

message = """Subject: Please take our survey
To: {recipient}
From: {sender}

Hi {name}, 

Thank you for agreeing to take our survey.  You will need to click on the link below in order
to access your personalized survey.  Each link is unique.  If you need to stop the survey and start again at a later time
you can just click the link again and it will take you to the point where you left off.

{link}

If that link doesnt work you can go to:
https://www.domain.com/logintosurvey/
and enter your personal code: {respondent_id}

Ciao! """
sender = "test@example.com"

with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.ehlo_or_helo_if_needed()
    server.login(login, password)
    with open("respondent-list.csv") as file:
        reader = csv.reader(file)
        next(reader)  # add this to skip the header row
        for name, email, link, respondent_id in reader:
            server.sendmail(
               sender,
                email,
                message.format(name=name, recipient=email, sender=sender, link=link, respondent_id=respondent_id)
            )
            print(f'Sent to {name}')

