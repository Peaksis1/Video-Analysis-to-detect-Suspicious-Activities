import smtplib
import string

def smtp_gmail(timestampList,email_to,subject):
    username = "susactivitydetectionteam@gmail.com"
    password = "prakhars"
    email_from = "Suspicion Detection Team"
     
    email_body = "\r\n".join([
  "From: Suspicion Detection Team",
  "To:"+email_to,
  "Subject: "+subject,
  "",
  timestampList
  ])
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.ehlo()
    server.sendmail(email_from, email_to, email_body)
    server.quit()