import eel
import requests

# Set web files folder and optionally specify which file types to check for
eel.init('web', allowed_extensions=['.js', '.html'])

# Define a function to get Lil Durk's latest songs using the Last.fm API
def get_lil_durk_songs():
    api_key = 'YOUR_API_KEY_HERE'
    artist = 'Lil Durk'
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={api_key}&format=json'
    response = requests.get(url)
    data = response.json()
    songs = []
    for track in data['toptracks']['track']:
        song_name = track['name']
        songs.append({'name': song_name})
    return songs

# Expose this function to Javascript
@eel.expose
def get_lil_durk_songs_py():
    return get_lil_durk_songs()

# Start the app
eel.start('index.html', size=(500, 300))
