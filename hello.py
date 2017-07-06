from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
	return render_template('index.html')

@app.route('/devices/0/turn_on', methods = ['POST'])
def turn_on():
    state = request.values.get('color')
    return render_template('index_1.html', state = state)

@app.route('/device_states', methods = ['POST'])
def change():
    state = request.values.get('color')
    return render_template('index_1.html', state=state)

if __name__ == "__main__":
    app.run(host = '0.0.0.0')