# Smart_plant
The used devices are:
-Raspberry 3b+
-Grove - Moisture Sensor V1.4 (https://wiki.seeedstudio.com/Grove-Moisture_Sensor/)
-Grove - Light Sensor v1.2 (https://wiki.seeedstudio.com/Grove-Light_Sensor/#:~:text=The%20Grove%20-%20Light%20sensor%20integrates,i.e.%20based%20on%20resistance%20value)
-Grove Base Hat for Raspberry Pi (https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/)



In order to run the code makes sure that the following packages work on your raspi:
-Json
-request
-datetime
-math
-sys
-time
-ADC
-isAlpha
-subprocess
-parse_http_list
-twython


Steps:
-set up the raspberry and Grove Base Hat
-insert the Moisture sensor at A2 and Light sensor at A0
-make sure that the said packages work on your raspi
-set up a Corlysis and Twitter account
-adjust the code (Corlysis token etc.)
-run the code
