from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename='logger/app.log', encoding='utf-8', level=logging.DEBUG)
@app.route('/')
def hello():
    app.logger.info('Processing default request')
    print("Hello from root path")
    return "welcome to the flask tutorials"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
