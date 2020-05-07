# -*- coding=utf-8 -*-
import yagmail

## https://myaccount.google.com/lesssecureapps

fromemail = ""
password = ""
yag = yagmail.SMTP(fromemail, password)

def sendMail(mail, title, content):
    contents = [content]
    yag.send(mail, title, contents)




