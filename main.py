#!/usr/bin/python
from curses.ascii import isalpha
import subprocess
from urllib.request import parse_http_list
import requests

l = subprocess.getoutput('cd grove.py && python3 ~/light_final.py 0')#excecudes shell command and gets the output of the executed script light_final.py
subprocess.run('cd ..', shell=True)#executes shell command which goes back to home directory

m = subprocess.getoutput('cd grove.py && python3 ~/moisture_final.py 2')#excecudes shell command and gets the output of the executed script moisture_final.py
subprocess.run('cd ..', shell=True)#executes shell command which goes back to home directory

#function for extracting only the actual values of the output of the executed shell commands. The output contains not only the moisture and light level,
#but also if the command was correctly executed. The function extracts only the light and moisture level by filtering all letters, etc. out and returning only values
def get_number(parameter):
    empty_string=""
    for x in range(len(parameter)):
        if parameter[x].isdigit():
            empty_string = empty_string + parameter[x] 
    return(int(empty_string))

def moisture_norm(m):
    if 0 <= m and m < 300:
        return(0) #dry
    elif 300 <= m and m < 600:
        return(1) #moist
    else:
        return(2) #wet


light_current = get_number(l)#filter for light value
moisture_current = get_number(m)#filter for moisture value
print("Light level:",light_current,"Moisture level:", moisture_current)

ss_sr = subprocess.getoutput(f'python3 ss_sr.py')
#executes shell command, which calls the sunrise and sunset script. Contains value whether or not the current time, is between sunrise and sunset
#If the current time is befor or after the sunset, then there is no point in tweeting the light level, as the user is either sleeping or natural light is not avaiabale
subprocess.run('cd ..', shell=True)#executes shell command which goes back to home directory
print("Is time between sunrise and sunset?",ss_sr)

url = 'http://corlysis.com:8087/write'#defines urls
params = {"db": "test", "u": "token", "p": "5f0b565048c9537d33b11efb0e9501ff"}#defines name and password of the db
payload = f"light light={light_current},moisture={moisture_current}\n"#defines payload
if ss_sr == "True": #since we look at the printed True of ss_sr.py the output doesn´t see it as a Boolean true
    r = requests.post(url, params=params, data=payload)#send light and mois>
    print(r)
else:
    print("Didn´t push to DB")


needs_plants_raw = subprocess.getoutput('python3 database_plants.py "Test plant"')
#executes the database_plants.py There a small database with different plants and there needs is located.
#gets the ouput for the called plant, which are moisture and light needs
subprocess.run('cd ..', shell=True)#executes shell command which goes back to home directory
needs_plants = needs_plants_raw.split(sep=" ")#creates a list out of the raw output of the plant database query

moisture_need = int(needs_plants[0])#gets the "first" element of the needs_plants variable which store the moisture level, 1 = moist     2 = dry    2 = wet
light_need = int(needs_plants[1])#gets the "second" element of the needs_plants variable which store the light level
moisture_current_comparable = moisture_norm(moisture_current)#function that "normalizes" the moisture level to 1 = moist     2 = dry    2 = wet, taken from https://wiki.seeedstudio.com/Grove-Moisture_Sensor/

light_mean = float(subprocess.getoutput(f'python3 light_mean.py'))

if light_mean < light_need:
    print("Tweeted: Put me in another spot")
    subprocess.getoutput(f'cd twitterbot && sudo python3 TwitterBot.py "Our calculations have come to the conclusion that the current place is not suitable for us. PLease consider putting us in a more sunny spot."')#executes shell command, which calls twitterbot to tweet
    subprocess.run('cd ..', shell=True)#executes shell command which goes back to home directory

#moisture must be transformed into numbers for comparison
if moisture_current_comparable < moisture_need:
    print("Tweeted: Water me")
    subprocess.getoutput(f'cd twitterbot && sudo python3 TwitterBot.py "As water is essential for our well being, we ask you politely to supply us with more of it."')#executes shell command, which calls twitterbot to tweet
    subprocess.run('cd ..', shell=True)#executes shell command which goes back to home directory
else:
    print("Tweeted: nothing")
    pass

