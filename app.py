import configparser
from flask import Flask, redirect, render_template, request, url_for
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
@app.route('/additem')
def add_item():
     return render_template('add_item.html')
#-------sql-----

#--------@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
	if request.method == 'POST':
		name = request.form['name']
		price = request.form['price']
		conn = sqlite3.connect('items.db')
		c = conn.cursor()
		c.execute('INSERT INTO items (name, price) VALUES (?, ?)', (name, price))
		conn.commit()
		conn.close()
		return 'Item added successfully!'
	else:
		return render_template('add_item.html')