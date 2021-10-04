import smtplib

'''
verizon: @vtext.com
att: @mms.att.net
tmobile: @tmomail.net
'''

email = "ece.4880.lab@gmail.com"
password = "KK5PF6qc9GKWhT"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)

def send_sms(number, message):
    server.sendmail(email, number, message)

#if __name__ == "__main__":
#    send_sms("6125997855@vtext.com", "test123")
    