
import sms_conf, json, time
from boltiot import Sms, Bolt
min_limit = 300
max_limit = 600
mybolt = Bolt(sms_conf.API_KEY, sms_conf.DEVICE_ID)
sms = Sms(sms_conf.SID, sms_conf.AUTH_TOKEN, sms_conf.TO_NUMBER, sms_conf.FROM_NUMBER)

while True:
    print("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    res = int(data['value'])
    temp = (100*res)/1024
    print("Sensor value is : " + str(temp))
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
