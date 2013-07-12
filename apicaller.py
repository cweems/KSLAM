import requests
import pprint
import json

queryparams = {

'country': 'Tanzania'

}

endpoint = 'http://explore.data.gov/resource/7swc-ittd.json'

response = requests.get(endpoint, params= queryparams)

data = response.json()

json_string = json.dumps(data)

pprint.pprint(json_string)