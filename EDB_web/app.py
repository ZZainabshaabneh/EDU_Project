from flask import Flask, render_template, jsonify, request,session,redirect,url_for
import pymongo  # Corrected import
from pymongo import MongoClient
import uuid
from passlib.hash import pbkdf2_sha256  # To encrypt password
app= Flask(__name__)
# Connect to the MongoDB, change the connection string per your MongoDB environment
client = pymongo.MongoClient("localhost",27017)

# Specify the database to be used
db = client.user_login_system

# Specify the collection to be used
collection = db.testcollection
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learn.html')
def layout():
    return render_template('learn.html')


@app.route('/Math_learn.html')
def learn():
    return render_template('Math_learn.html', custom_css="Math_learn")



@app.route('/login.html')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        success, user = sign_in(db, email, password)  # Modify to accept user object
        if success:
            session['email'] = email
            user_document = db.users.find_one({'email': email})
            if user_document:
                username = user_document['username']
                session['username'] = username
            role = user.get('role')  # Access the role from the user object
            session['role'] = role  # Store the role in the session
            if role == 'provider':
                return redirect(url_for('provider_dashboard'))
            elif role == 'seeker':
                return redirect(url_for('seeker_dashboard'))
        else:
            error_message = "Invalid email or password"
            return render_template('signin.html', error_message=error_message)
    return render_template('signin.html', role=request.args.get('role'))

@app.route('/signup.html')
def signup():
    if request.method == 'POST':
        role = request.args.get('role')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        success, error_message = sign_up(db, role)  # Pass role to sign_up function
        if success:
            session['email'] = email
            session['username'] = username
            return redirect(url_for('signin'))
        else:
            return render_template('signup.html', role=role, error_message=error_message)
    return render_template('signup.html', role=request.args.get('role'))


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blogger')
def blog():
    return render_template('blog.html')

@app.route('/tajweed')
def Tajweed():
    return render_template('tajweed.html')

@app.route('/Math.html')
def Math():
    return render_template('Math.html')

@app.route('/languges')
def languges():
    return render_template('languges.html')

@app.route('/Test')
def Test():
    return render_template('Test.html')

@app.route('/Math_test.html')
def Math_test():
    return render_template('Math_test.html', custom_css="math_test")

@app.route('/Math_Learn_dobel.html')
def Math_Learn_dobel():
    return render_template('Math_Learn_dobel.html', custom_css="Math_learn" , custom_css2="Math_learn_drag1")


@app.route('/practice1.html')
def practice1():
    return render_template('practice1.html', custom_css="practice1" )

if __name__=='__main__':
    
    app.run(debug=True)