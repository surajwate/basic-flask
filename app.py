from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'THISISASECRET'


def connect_db():
    sql = sqlite3.connect('D:\\Suraj\\Coding\\python\\databases\\fadb')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'Stranger'})
@app.route('/home/<name>', methods=['GET', 'POST'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False, colors=['blue', 'orange', 'yellow', 'green'])


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
    name = session['name']
    if request.method == 'GET':
        return render_template('form.html', name=name)
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


@app.route('/results')
def results():
    db = get_db()
    cur = db.execute('SELECT id, name, location FROM users')
    results = cur.fetchall()
    return "<h1>{} : {} from {}.</h1>".format(results[0]['id'], results[0]['name'], results[0]['location'])


if __name__ == '__main__':
    app.run()
