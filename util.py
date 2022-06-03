import pandas as pd
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def readcompany():
    ea = pd.read_excel("dataset/email.xlsx", dtype={'Name': str, 'Email': str, 'Client':str,'yes/no': str})
    nr = ea.loc[ea['Replied'] == 'no']
    return nr


def sendemail(name, client, email):

    #if you use gmail or other email, you have to change "smtp.zohomail.com" and 465 to smtp server of your email and port number. you can find it by googling "smtp server configuration - domain of email"
    #if you need help, you can contact me.
    email_from  = 'your email address' #your email and password, *make sure you set up SMTP(google changed SMTP, so we have to pay for it)
    password = 'your password of email address' 


    msg = MIMEMultipart()
    msg['From'] = email_from #your email address
    msg['To'] = email
    msg['Subject'] = f'test subject' #change this string to subject of email


    msg_string = ("""
Dear {1},

This is the test email for company {0}.

Sincerely,
Example

    """.format(name,client) #text in email
    )#{0} is the name of company and {1} is the name of client

    msg.attach(MIMEText(msg_string))

    email_string = msg.as_string()

    context_ = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.zoho.com", 465, context= context_) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email, email_string)

    return


