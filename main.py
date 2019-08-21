from flask import Flask, request, redirect, render_template



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

@app.route("/home")
def home():
    if request.method == "POST":

        radio_error = ''

        option = request.form.get("hair-type")

        if not option:
            radio_error = "must select hair type"

        

        if option == ("hair3a"):
            return redirect('/learn') 
        else:
            return render_template('home.html')


     


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


app.run()    