from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import cgi





app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hair-we-go-python:liftoff@localhost:8889/hair-we-go-python'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Hello World"

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        option = request.form['hair']
        return redirect(url_for('select', option=option))
    return render_template('home.html')    


@app.route('/<option>')
def select(option):
    return render_template(option)



        

            


     


@app.route("/learn")
def learn():
    return render_template('learn.html')

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():

    if request.method== 'POST':
        username = request.form['username']  
        username_error = ''


        if len(username) == 0:
            username_error = 'Can not be blank'

        if len(username) < 3:
            username_error = 'Must be more than 3 characters'


        if not username_error:
            return redirect('/home')    
        else:
            return render_template('signup.html', username=username, username_error=username_error)

    return render_template('signup.html')  

@app.route("/validate", methods=['POST', 'GET'])
def validate_radio_buttons():
    if request.method == "POST":

        radio_error = ''

        option = request.form['hair-type']

        if not option:
            radio_error = "must select hair type"

        

        if option == hair3a:
            return redirect('/learn')    


if __name__ == '__main__':
    app.run()    