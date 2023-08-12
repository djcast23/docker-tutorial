from flask import Flask # Import Flask

app = Flask(__name__) # Initialize Flask

@app.route('/') # Setup an endpoint, much like an API
def hello():
    return "Hello, Dockerized Flask App!" # Tells the server to return "Hello, Dockerized Flask App!"
                                          # when a request is sent to the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) # Runs the flask app on Port 80 (which is forwarded to port 8080 outside the container)
