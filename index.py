from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is a simple Flask API running on EC2!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
