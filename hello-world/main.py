import eel

# Set web files folder as web interface
eel.init('web')

# Define a function to send data from Python to JavaScript
@eel.expose
def send_data_from_python(data):
    print(f"Received data from JavaScript: {data}")
    return f"Hello, {data} from Python!"

# Define a function to send data from JavaScript to Python
@eel.expose
def send_data_from_js(data):
    print(f"Received data from JavaScript: {data}")
    return f"Hello, {data} from Python!"

# Define a function to start the Eel app
def start_app():
    eel.start('index.html', size=(300, 200))

# Start the Eel app
if __name__ == '__main__':
    start_app()
