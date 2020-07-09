from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="")
location = geolocator.geocode("19 ")
print(location.address)

lat = location.latitude
lon = location.longitude

print((location.latitude, location.longitude)) 