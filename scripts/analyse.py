import requests
import json

def analyse(text):
	subscription_key = '9c5b70f91fc240a088740f20b0117f57'
	assert subscription_key
	text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
	sentiment_api_url = text_analytics_base_url + "sentiment"
	print(sentiment_api_url)
	documents = {'documents' : [
	  {'id': '1', 'language': 'en', 'text': text}
	]}
	headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
	response  = requests.post(sentiment_api_url, headers=headers, json=documents)
	jdata = json.loads(response.content)
	return (jdata['documents'][0]['score'])

