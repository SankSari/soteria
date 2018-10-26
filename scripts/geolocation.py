from math import radians, cos, sin, asin, sqrt
import requests, json
import geocoder

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km
    # print (km)
    # return km, lon1, lat1, lon2, lat2

def myLoc():
    g = geocoder.ip('me')
    return (g.latlng)

def getNearbyPlaces(place):
    loc = myLoc()
    lat = str(loc[0])
    lon = str(loc[1])
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ lat + ',' + lon + '&radius=1000&type=' + place + '&key=AIzaSyAcuwTIAN38WlfEwQqxYdLhLWN476BFExI'
    response = requests.get(url)
    jdata = json.loads(response.content)
    # print (json.dumps(jdata, indent=4, sort_keys=True))
    placesList = []
    info = {}
    count = 0
    for data in jdata['results']:
        if count == 5:
            break
        # print(jdata['results'][count]['geometry']['location']['lat'])
        dlat = float(jdata['results'][count]['geometry']['location']['lat'])
        dlon = float(jdata['results'][count]['geometry']['location']['lat'])
        dist = haversine(loc[1], loc[0], dlon, dlat)
        name = jdata['results'][count]['name']
        print (dist)
        print (name)
        info = {
            'name' : name,
            'distance' : dist 
        }
        placesList.append(info)
        count = count + 1
    return placesList
