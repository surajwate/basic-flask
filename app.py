from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'Stranger'})
@app.route('/home/<name>', methods=['GET', 'POST'])
def home(name):
    return '<h1>Hello {}. You are on the home page of python app.</h1>'.format(name)


@app.route('/json')
def json():
    return jsonify({'key1': 'value1', 'key2': [1, 2, 3]})


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return "<h1>Hell {} from {}. You are on query page.</h1>".format(name, location)


@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return """
                <form method="POST" action='/theform'>
                    <input type="text" name="name">
                    <input type="text" name="location">
                    <input type="submit" value="Submit">
                </form>
        """
    else:
        name = request.form['name']
        location = request.form['location']
        return "<h1>Hello {} from {}. You have successfully submitted the form.</h1>".format(name, location)
    
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
    return jsonify({'try' : 'error', 'Name' : name, 'Location' : location, 'color' : color[1]}) 

if __name__ == '__main__':
    app.run(debug=True)
