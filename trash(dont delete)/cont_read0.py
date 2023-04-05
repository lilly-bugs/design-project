from flask import Flask
import client

app = Flask(__name__)

@app.route('/')
def temp():
    temp = client.return_temp()
    
    return temp

if __name__ == "__main__":
    app.run(host='0.0.0.0')