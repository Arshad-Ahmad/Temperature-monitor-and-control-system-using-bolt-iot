import requests
import json, time 

a_key = ""
d_id = ""

telegram_chat_id = ""
telegram_bot_id = ""

mybolt = Bolt(a_key, d_id)

def get_sensor_value_from_pin(pin):
    
    try:
        response = mybolt.analogRead(A0)
        data = json.loads(response)
        if data["success"] != 1:
            print("Request not successfull")
            print("This is the response->", data)
            return -999
        sensor_value = int(data["value"])
        return sensor_value
    except Exception as e:
        print("Something went wrong when returning the sensor value")
        print(e)
        return -999
