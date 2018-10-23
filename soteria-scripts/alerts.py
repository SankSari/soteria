import requests
import json
import pprint
from analyse import analyse

def predictEvent(type, place = 'IN'):
	url = 'https://api.predicthq.com/v1/events/?q='+type
	response = requests.get(url, headers={'Authorization': 'Bearer 38UqPIzYkYeg8vwBgQ70liqVfpCG3W'})
	print(response)
	jdata = json.loads(response.content)
	# print (json.dumps(jdata['results'], indent=4, sort_keys=True))
	jresults = jdata['results']
	i = 0
	for key in jresults:
		if(jresults[i]['category'] == 'terror' and jresults[i]['country'] == place):
			print(jresults[i]['description'])
		i = i+1


def predictCalamity(type, place = 'India'):
	url = 'https://api.reliefweb.int/v1/reports?appname=apidoc&filter[field]=country&filter[value]='+place+'&query[value]='+type
	response = requests.get(url)
	jdata = json.loads(response.content)
	i = 0
	for key in jdata['data']:
		print(jdata['data'][i]['fields']['title'])
		i = i + 1
	# print (json.dumps(jdata, indent=4, sort_keys=True))

def msnewsSearch(type, place = 'india'):
	search_url = "https://api.cognitive.microsoft.com/bing/v7.0/news/search"
	search_term = type + '+' + place
	headers = {"Ocp-Apim-Subscription-Key" : '582a783225a34e748c9b567dc76a536c'}
	params  = {"q": search_term, "textDecorations": True, "textFormat": "Html"}
	response = requests.get(search_url, headers=headers, params=params)
	jdata = json.loads(response.content)
	i = 0
	for key in jdata['value']:
		print(jdata['value'][i]['description'])
		i = i + 1
	# print (json.dumps(jdata, indent=4, sort_keys=True))


# predictEvent('terrorist', 'IN')
# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# predictCalamity('earthquake', 'India')
# msnewsSearch('earthquake', 'india')
