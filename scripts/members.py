from geolocation import haversine

def findMembers(volunteer, memberList):
	volFinal = []
	memFinal = []
	memcount = 0
	for member in memberList:
		dist = haversine(memberList[memcount]['long'], memberList[memcount]['lat'], volunteer['long'], volunteer['lat'])
		if dist >= 2500:
			volFinal.append(memcount+1)
		memcount = memcount + 1

	print (volFinal)

findMembers({ 'id': 1, 'lat': 40, 'long': 40 }, [{ 'id': 1, 'lat': 20, 'long': 20 }, { 'id': 2, 'lat': 30, 'long': 30 }])