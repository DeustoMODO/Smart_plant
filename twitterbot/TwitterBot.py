
#!/usr/bin/env python
import sys
from twython import Twython

#Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 'WWfy3ywvd2qY7y39hcRGIgSNS'
CONSUMER_SECRET = 'TAKDjMxfiZ7NS2b5a83z0lV9TuaKZxRiYnYqHMVu8XAmPc8Mho'
bearer_token = "AAAAAAAAAAAAAAAAAAAAABV8jgEAAAAAsGKteiv3smhFIsPyhOnjdwt7FbI%3Dx8VuTWhIWuPaYxZrpAGsqPFcYYabemBfjn2OTHor7AcvW0dNMf"
ACCESS_KEY = '1595116674021298184-wFGZjhq5qRHYRhaef0PTex2L82UI1b'
ACCESS_SECRET = 'HtKGq5zBrcfiPNRlujJqdRUlN512TO63KuLH4YOXTXiIK'

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

#Using our newly created object, utilize the update_status to send in the text passed in through CMD
api.update_status(status=sys.argv[1])
