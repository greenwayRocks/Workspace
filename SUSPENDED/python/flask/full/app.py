from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'

def connect_db():
    sql = sqlite3.connect('data.db')
    sql.row_factory = sqlite3.Row # Get dicts instead of tuples
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
    session.pop('name', None)
    return '<h1>Hello, world!</h1>'

@app.route('/home', defaults={'name': 'world'})
@app.route('/home/<string:name>')
def home(name):
    session['name'] = name
    db = get_db()
    cur = db.execute('select id, name, location from users;')
    results = cur.fetchall()
    return render_template('home.html', name=name, display=False, mylist=['one', 'two', 'three', 'four'],
     mydict={'name': 'Sarah', 'location': 'California'}, results=results)

@app.route('/json')
def json():
    if 'name' not in session:
        name = 'notInSession'
    else:
        name = session['name']
    return jsonify({'username': name, 'fruits': ['mangoes', 'apples']})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}.You are from {}. You are on the query page!</h1>'.format(name, location)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form.get('name')
        location = request.form.get('location')

        db = get_db()
        db.execute('insert into users (name, location) values (?, ?);', [name, location])
        db.commit()
        return redirect(url_for('home'))
        #return '<h1>Hello, {}. You are from {}. You have submitted the form successfully!</h1>'.format(name, location)
        #return rediract(url_for('home', name=name))
        #return redirect(url_for('query', name=name, location=location))

    
    
@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']

    return jsonify({'result': 'Success', 'name': name, 'location': location, 'random': randomlist})

@app.route('/viewresults')
def viewresults():
    db = get_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()
    id, name, location = results[0]
    return '<h1>The ID is {}. The name is {}. The location is {}.</h1>'.format(id, name, location)

if __name__ == '__main__':
    app.run()