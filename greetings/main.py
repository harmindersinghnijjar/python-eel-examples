import eel
from screeninfo import get_monitors

# Set web files folder and optionally specify which file types to check for eel.expose()
eel.init('web')

# Expose functions to JavaScript
@eel.expose
def greet(name):
    return f"Hello, {name}!"

# Set the window size to be the same as the primary monitor resolution
monitors = get_monitors()
primary_monitor = monitors[0]
# eel_kwargs = {
#     'host': 'localhost',
#     'port': 8000,
#     'size': (primary_monitor.width, primary_monitor.height),
#     'borderless': True,
# }

eel.start('index.html', host='localhost', port=8000, size=(primary_monitor.width, primary_monitor.height), borderless=True)

