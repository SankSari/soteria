from twilio.rest import Client 

def smsAlerts(message, repno):
	account_sid = 'AC940c088a5bad73e4d4fa46e0f9b738d6' 
	auth_token = 'e857cca310317e6dc55e00399eb555a6' 
	client = Client(account_sid, auth_token) 
	repno = '+91' + repno
	message = client.messages.create( 
	                              from_='+17154966191',  
	                              body=message,      
	                              to=repno
	                          ) 
	 
	print(message.sid)

smsAlerts('this is so cool indeed', '8172003164')
