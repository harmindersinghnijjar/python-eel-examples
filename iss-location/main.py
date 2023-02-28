import eel
import requests

# Set web files folder and optionally specify which file types to check for
eel.init('web', allowed_extensions=['.js', '.html'])

# Define a function to get the current location of the ISS using the Open Notify API
def get_iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    data = response.json()
    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']
    return {'longitude': longitude, 'latitude': latitude}

# Expose this function to Javascript
@eel.expose
def get_iss_location_py():
    return get_iss_location()

# Start the app
eel.start('index.html', size=(500, 300))
