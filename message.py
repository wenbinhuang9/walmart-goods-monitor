# -*- coding=utf-8 -*-
import yagmail

## https://myaccount.google.com/lesssecureapps
yag = yagmail.SMTP("benpovertykaka@gmail.com", "Qaz!@#456")

def sendMail(mail, title, content):
    contents = [content]
    yag.send(mail, title, contents)


