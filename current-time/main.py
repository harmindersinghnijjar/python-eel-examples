import eel
import datetime

# Set web files folder as web interface
eel.init('web')

# Define a function to get the current time
@eel.expose
def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time

# Define a function to start the Eel app
def start_app():
    eel.start('index.html', size=(300, 200))

# Start the Eel app
if __name__ == '__main__':
    start_app()
