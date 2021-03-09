from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'THISISASECRET'


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'Stranger'})
@app.route('/home/<name>', methods=['GET', 'POST'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False)


@app.route('/json')
def json():
    name = session['name']
    return jsonify({'key1': 'value1', 'key2': [1, 2, 3], 'Name': name})


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return "<h1>Hell {} from {}. You are on query page.</h1>".format(name, location)


@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        '''
        location = request.form['location']
        return "<h1>Hello {} from {}. You have successfully submitted the form.</h1>".format(name, location)
    '''
        return redirect(url_for('home', name=name))


"""
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return "<h1>Hello {} from {}. You have successfully submitted the form.</h1>".format(name, location)
"""


@app.route('/jsonprocess', methods=['POST'])
def jsonprocess():
    data = request.get_json()
    name = data['name']
    location = data['location']
    color = data['color']
    return jsonify({'try': 'error', 'Name': name, 'Location': location, 'color': color[1]})


if __name__ == '__main__':
    app.run()
