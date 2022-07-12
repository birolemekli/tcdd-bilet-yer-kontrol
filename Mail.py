# coding=utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

class Mail:
    def __init__(self,mail_to,subject):
        self.__smtp_host="smtp.x.com" # ie : smtp.gmail.com
        self.__mail_from="your mail" #ie : youremail@gmail.com
        self.__mail_from_password="your password" # ie : 123456
        self.mail_to=mail_to
        self.subject=subject

    def sendMail(self,timee):
        try:
            msg = MIMEMultipart()
            password = self.__mail_from_password
            msg['From'] =self.__mail_from
            msg['To'] = self.mail_to
            msg['Subject'] = self.subject 
            msg.attach(MIMEText(self.subject))
            msg.attach(MIMEText(timee))
            server = smtplib.SMTP(self.__smtp_host)
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg["To"].split(","), msg.as_string())
            print ('Mail gonderildi...')
        except Exception as e:
            print(e)
            print ('Mail göndermede bir sorun meydana geldi')

    def getHost(self):
        return self.__smtp_host

    def setHost(self,stmpHost):
        self.__smtp_host=stmpHost

    def getFrom(self):
        return self.__mail_from

    def setFrom(self,mailFrom):
        self.__mail_from=mailFrom

    def setFromPassword(self,mailFromPassword):
        self.__mail_from_password=mailFromPassword
