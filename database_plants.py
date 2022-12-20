import json
import sys


def check(names_plants, user_plant):
    if user_plant in names_plants:
        print(plants[user_plant]["Water"],plants[user_plant]["Light"])
    else:
        print("ERROR, wrong name")

#below is a small database in json format , 1 = moist, 2 = dry 
plants_json = '{"Test plant":{"Water":"1","Light":"500"},"Aechmea fasciata":{"Water":"1","Light":"1614"},"Anthurium sp.":{"Water":"1","Light":"1614"},"Aspidistra elatior":{"Water":"1","Light":"500"},"Begonia sp.":{"Water":"1","Light":"10764"},"Calathea sp":{"Water":"1","Light":"1614"},"Chlorophytum elatum":{"Water":"1","Light":"10764"},"Cordyline fruticosa":{"Water":"1","Light":"1614"},"Nephrolepsis cordifolia":{"Water":"1","Light":"1614"},"Sansevieria sp.":{"Water":"2","Light":"500"}}'
plants = json.loads(plants_json)#loading the json format
names_plant = "Test plant, Aechmea fasciata, Anthurium sp., Aspidistra elatior, Begonia sp., Calathea sp, Chlorophytum elatum, Cordyline fruticosa, Nephrolepsis cordifolia, Sansevieria sp."
#plants inside the database
user_plant = sys.argv[1]#the user chosses the name of the plant

check(names_plant, user_plant)
