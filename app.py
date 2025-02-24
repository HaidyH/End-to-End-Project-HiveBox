from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is running!"

@app.route("/version")  # This should be placed BEFORE app.run()
def version():
    return "v0.0.1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)