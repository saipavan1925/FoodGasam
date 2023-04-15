import configparser
from multiprocessing import connection
from flask import Flask, Response, redirect, render_template, request, url_for

import sqlite3
app = Flask(__name__)




@app.route("/")
def home():
   return "Hello, Flask!"

@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/aboutus/")
def aboutus():
    return render_template("aboutus.html")


@app.route("/Menu/")
def Menu():
    return render_template('Menu.html')

@app.route('/signin')
def signin():
    # code to execute when the /signin endpoint is accessed
    return render_template('signup.html')

@app.route('/login')
def login():
    # code to execute when the /login endpoint is accessed
    return render_template('login.html')

#---------- Specials----
@app.route('/Dosa')
def Dosa():
    return render_template('Dosa.html')
@app.route('/Paneer_Tikka')
def paneer_tikka():
    return render_template('Paneer_Tikka.html')
#------------SignUp----
@app.route('/signup')
def signup():
    return render_template('signup.html')
#------------add_item--

#-------sql-----

import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

"""conn.execute('''CREATE TABLE items
             (id INTEGER PRIMARY KEY,
             category TEXT,
             item_name TEXT,
             price REAL,
             item_image BLOB);''')
print("Table created successfully")"""

conn.close()

@app.route('/enternew')
def new_item():
   return render_template('item.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        try:
            category = request.form['category']
            item_name = request.form['item_name']
            price = request.form['price']
            item_image = request.files['item_image'].read()
            
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO items (category, item_name, price, item_image) VALUES (?, ?, ?, ?)", 
                            (category, item_name, price, item_image))
                
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("result.html", msg=msg)


   
@app.route('/view_items_by_category', methods=['GET'])
def view_items_by_category():
    category = request.args.get('category')
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT item_name, price, item_image FROM items WHERE category = ?", (category,))
        rows = cur.fetchall()
    return render_template('view_items_by_category.html', rows=rows)
































#------to delete the db--------------   
"""import os
import sqlite3

# Close any open connections to the database
conn = sqlite3.connect('database.db')
conn.close()

# Drop the items table
conn = sqlite3.connect('database.db')
conn.execute("DROP TABLE items")
conn.close()

# Delete the database file
os.remove('database.db')"""
