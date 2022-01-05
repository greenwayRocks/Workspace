from flask import Flask, render_template, url_for,g, request
import sqlite3
from datetime import datetime
import re

app = Flask(__name__)

def db_date(date):
    assert re.match(r'^[\d]+-[\d]+-[\d]+$', date)
    new_date = datetime.strptime(date, '%Y-%m-%d')
    final_date = datetime.strftime(new_date, '%Y%m%d')
    return final_date

# -------------------------------
def connect_db():
    sql = sqlite3.connect('food_log.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# -------------------------------

@app.route('/', methods=['GET','POST'])
def index():
    db = get_db()
    if request.method == 'POST':
        day = request.form['day'] # assuming date format is YYYY-MM-DD
        dt = db_date(day)
        db.execute('insert into log_date (entry_date) values (?);', [dt])
        db.commit()

    cur = db.execute('select entry_date from log_date order by entry_date desc;')
    results = cur.fetchall()
    dates = []

    for i in results:
        item = {}
        temp = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        item['entry_date'] = datetime.strftime(temp, '%B %d, %Y')
        dates.append(item)
    
    return render_template('home.html', dates=dates)

@app.route('/view')
def view():
    return render_template('day.html')

@app.route('/food', methods=['GET', 'POST'])
def food():
    db = get_db()

    if request.method == 'POST':
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbs = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protein * 4 + carbs * 4 + fat * 9 
        db.execute('insert into food (name, protein, carbs, fat, calories) values (?, ?, ?, ?, ?);', [name, protein, carbs, fat, calories])
        db.commit()
    
    cur = db.execute('select name, protein, carbs, fat, calories from food;')
    results = cur.fetchall()

    return render_template('add_food.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)