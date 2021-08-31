from boltiot import Bolt, Sms
import warning
import telegram_alert


a_key = "607bfc05-098d-4571-80b3-9644261c0b30"
d_id = "BOLT1117077"
mybolt = Bolt(a_key, d_id)

def device_status():
    response = mybolt.isOnline()
    print(response)

def temp_reading():
        print("Reading sensor value")
        response = mybolt.analogRead('A0')
        data = json.loads(response)
        res = int(data['value'])
        temp = (100*res)/1024
        print("Sensor value is : " + str(temp))

def SMS_alert():
    min_limit = 300
    max_limit = 600
    mybolt = Bolt(sms_conf.API_KEY, sms_conf.DEVICE_ID)
    sms = Sms(sms_conf.SID, sms_conf.AUTH_TOKEN, sms_conf.TO_NUMBER, sms_conf.FROM_NUMBER)

    while True:
        try:
            sensor_value = int(data['value'])
            if sensor_value > max_limit or sensor_value < min_limit:
                print("Making request to send SMS")
                response = sms.send_sms("The Current Temp sensor value is " +str (sensor_value))
                print("Response received from Twilio is :" + str(response))
                print("Status of SMS at Twilio is :" + str(response.status))
        except Exception as e:
                            print("Error occured: Below are the details ")
                            print(e)
        time.sleep(10)

def Mail_alert():
    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You'''
    #The mail addresses and password
    sender_address = (mail_conf.m_id)
    sender_pass = (mail_conf.m_pas)
    receiver_address = 'arsh7755868254@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Temp alert.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'TEMP'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

    
if __name__ == '__main__' :
    if temp > max_limit or temp < min_limit :
        warning()
        telegram_alert()
        Mail_alert()
        SMS_alert()
