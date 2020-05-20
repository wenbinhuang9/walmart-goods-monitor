

import yagmail
import  os
import sys

usename = ""
pwd = ""
yag = yagmail.SMTP(usename, pwd)


def sendMail(mail, title, content):
    contents = [content]
    yag.send(mail, title, contents)


def main(argv):
    filname = argv[1]
    mail = argv[2]

    dir = os.getcwd()

    filepath = dir + "/" + filname

    sendMail(mail, filname, filepath)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("please input filename and mail")

    main(sys.argv)

sendMail("fdf", "fa", "fdaf")