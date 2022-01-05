from flask import Flask, render_template, request, url_for, redirect, g
import sqlite3

app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('new.db')
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
    db = get_db()
    cur = db.execute('select id, name, location from users;')
    results = cur.fetchall()
    return render_template('index.html', results=results)

@app.route('/form', methods=["POST", "GET"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        name = request.form.get('name')
        location = request.form.get('location')
        # Store in database!
        db = get_db()
        db.execute('insert into users (name, location) values (?, ?);', [name, location])
        db.commit()
        
        return redirect(url_for('index')) 


if __name__ == '__main__':
    app.run(debug=True)