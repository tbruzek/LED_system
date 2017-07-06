from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
	return render_template('index.html')

@app.route('/devices/0/turn_on', methods = ['POST'])
def turn_on():
    state = request.form['255,255,000']
    return render_template('index_1.html', state = state)

#@app.route('/device_states', methods = ['POST'])
#def change():


if __name__ == "__main__":
    app.run(host = '0.0.0.0')