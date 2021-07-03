import requests

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=Temp_alert&message=Temperature Cross the threshold&language=english&route=p&numbers=8004963616"
headers = {
'authorization': "9SQnXMj0NkdYCKza8TpyDR1sPHIugGxLAr7Vtm6JiZqEUFl2hbDcKFH1fhgwCAebzjlUYp0Vy7sZRQ6r",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
