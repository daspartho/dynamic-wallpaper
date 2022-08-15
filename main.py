import geocoder

def get_lat_lng():
    g = geocoder.ip('me')
    return g.latlng