from flask import Flask

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def index1():
    return "CICD is completed"


@app.route('/', methods=['GET', 'POST'])
def index():
    return "CICD is running2"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
