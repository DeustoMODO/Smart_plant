import requests
import json

url = 'https://corlysis.com:8086/query'

headersJson = {
    'Accept': 'application/json',
}

params = {
    'db': 'test',
    'q': 'select light from light',
}

responseJson = requests.get(
    url,
    params=params,
    headers=headersJson,
    auth=('token', '5f0b565048c9537d33b11efb0e9501ff')
)

liste = json.loads(responseJson.text)["results"][0]["series"][0]["values"]
light_values = []
for i in range(len(liste)):
    light_values.append(liste[i][1])

print(sum(light_values)/len(liste))