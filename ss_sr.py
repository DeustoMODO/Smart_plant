import json
import requests
from datetime import datetime

#https://sunrise-sunset.org/api <- sunset sunrise api
sunset_sunrise = requests.get('https://api.sunrise-sunset.org/json?lat=43.2630&lng=2.9350&formatted=1')#gets json string through API
ss_sr = json.loads(sunset_sunrise.text)#encodes string
sunrise = datetime.strptime(ss_sr["results"]["sunrise"], "%I:%M:%S %p")#gets and transforms sunrise data, from encoded string, to time
sunset = datetime.strptime(ss_sr["results"]["sunset"], "%I:%M:%S %p")

now = datetime.now()#gets current date and time 
print(now.time() > sunrise.time() and  now.time() < sunset.time())# compares current time with sunrise and sunset time
#is current time "bigger" than sunrise time and "lower" than sunset time? <- is the current time between sunrise and sunset?
