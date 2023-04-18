from flask import Flask, get_flashed_messages, render_template, url_for, request, session, logging, redirect, flash, make_response
import sqlalchemy, random, string
from sqlalchemy.orm import scoped_session,sessionmaker
    
app = Flask(__name__)
app.secret_key = '9AajrQh98Ch3jCvQURzK'
authtoken = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(25))

#create connection to DB
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://admin:dHXZjEyfac423VZmeyqNnFBrRR64zjKM@127.0.0.1:3306/summitworks")
db = scoped_session(sessionmaker(bind=engine))

def get_comments():
    results = []
    select_all = 'SELECT comment FROM comments'
    for (comment,) in db.execute(select_all).fetchall():
        results.append(comment)
    return results

#route to index.html
@app.route('/')
def index():
    return render_template('index.html')

#route to login.html, handle POST data from login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        usernameSQL = db.execute(f"SELECT username FROM users WHERE username=\'{username}\' AND password=\'{password}\'").fetchone()

        if usernameSQL == None:
            error = "Invalid credentials." #implement flash later
        else:
            if usernameSQL:
                resp = make_response(redirect('welcome'))
                resp.set_cookie(b'authtoken', authtoken.encode('UTF-8'))
                return resp #redirect to welcome page
            else:
                error = "Invalid credentials."
            
    return render_template('login.html',error=error)

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    print(request.cookies)
    if 'flag' in request.cookies:
        comments = get_comments()
        return render_template('welcome.html', comments=comments)
    if authtoken in request.cookies["authtoken"]:
        if request.method=="POST":
            if request.form.get('comment'):
                db.execute(f'INSERT INTO comments (comment) VALUES (\"{request.form["comment"]}\");')
                db.commit()
            else:
                db.execute('DELETE FROM comments')
                db.commit()
            
        comments = get_comments()

        return render_template('welcome.html', comments=comments)
    else:
        return redirect('/login')

