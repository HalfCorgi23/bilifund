from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def start_interface_service():
    app.run()

if __name__ == '__main__':
    start_interface_service()