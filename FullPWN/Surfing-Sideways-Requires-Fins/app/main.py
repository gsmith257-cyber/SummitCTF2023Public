#!/bin/python

import os
import sqlite3
import getuser
import requests

from flask import Flask
from flask import redirect
from flask import request
import urllib.parse

app = Flask(__name__)

app.secret_key = 'gn7u484njgfb893bf3f3u'

DATABASE_PATH = os.path.join('/src/', 'db.sqlite')


def init():
    users = [
        ('admin', 'f0b26b3623af0cf78cad7fe752905f6f', '123'),
        ('annoyingUserThatAllAdminsHate', '7F2ABABA423061C509F4923DD04B6CF1', '123')
    ]
    #connect to database
    conn = sqlite3.connect(DATABASE_PATH)
    #add users to user table
    cur = conn.cursor()
    #clear the database
    cur.execute("DROP TABLE IF EXISTS user")
    cur.execute("CREATE TABLE IF NOT EXISTS user(username VARCHAR(32), password VARCHAR(32), flag VARCHAR(32) )")
    #add users to database
    cur.executemany('INSERT INTO user VALUES(?,?,?)', users)
    #cur = conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS user(username VARCHAR(32), password VARCHAR(32), flag VARCHAR(32) )")
    #cur.executemany('INSERT INTO user VALUES(?,?,?)', users)
    conn.commit()
    conn.close()


def login_page():
    return '''<html><h1>Login</h1>
<form method="GET" action="/login">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username">

  <label for="password">Password:</label>
  <input type="password" id="password" name="password">

  <input type="submit" value="Login">
</form>
</html>
    '''

@app.route('/')
def index():
    init()
    if request.remote_addr != '127.0.0.1' and request.remote_addr != 'localhost' and request.remote_addr != '2130706433' and request.remote_addr != '0.0.0.0':
        return '''<html><h1>Down Detector Flask Site (Internal)</h1>
    <form action="/check" method="POST" style="margin: 0 auto; width:140px;">
    <p><input name="url" placeholder="Check if site is down or login at /admin if your an admin" type="text" /></p>
    <input name="submit" type="submit" />
    </form>
    </html>'''
#return html for a down detector page that shows the status of the requested site and what was returned with a get request
    return '''<html><h1>Down Detector Flask Site</h1>
    <form action="/check" method="POST" style="margin: 0 auto; width:140px;">
    <p><input name="url" placeholder="Check if site is down" type="text" /></p>
    <input name="submit" type="submit" />
    </form>
    </html>'''

@app.route('/check', methods=['POST'])
def check():
    #get the value of the url from the user
    url = request.form['url']
    #check if url contains localhost or more than 2 periods
    if 'localhost' in url or url.count('.') > 2:
        return 'Invalid URL'
    #check if the url contains http or https
    if 'http://' not in url and 'https://' not in url:
        #if the url does not contain http or https, add http to the url
        url = 'http://' + url
    try:
        #check if the url is down and follow redirects
        r = requests.get(url, allow_redirects=True)
        #if the url is down, return the status code and the text
        if r.status_code != 200:
            return 'The site is down. Status code: ' + str(r.status_code) + '\n Text: ' + r.text
        #if the url is up, return the status code and the text
        else:
            return 'The site is up. Status code: ' + str(r.status_code) + '\n Text: ' + r.text
    #if the url is not valid, return invalid url
    except:
        return 'Invalid Site'


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.remote_addr != '127.0.0.1' and request.remote_addr != 'localhost' and request.remote_addr != '2130706433' and request.remote_addr != '0.0.0.0':
        #return a 403 error and a message if the user is not on the local host and print their ip
        return 'You are not on the local host. Your IP is ' + request.remote_addr
        #abort(403)
    if request.method == 'GET':
        #return the the entire request
        if 'arg' in request.args:
            #check if the arg added to url == 'fakeFlag%7BI_h4te_th3s3_4dm1n5%7D':
            if request.args.get('arg') == '123':
                #if the cookie is the admin flag, return the flag and a table of the users and hashes
                return '<html><h1>Welcome, admin</h1><table><tr><th>Username</th><th>Password</th><th>Flag</th></tr><tr><td>admin</td><td>F0B26B3623AF0CF78CAD7FE752905F6F</td><td>SummitCTF\{I_h4te_th3s3_4dm1n5\}</td></tr><tr><td>annoyingUserThatAllAdminsHate</td><td>7F2ABABA423061C509F4923DD04B6CF1</td><td>SummitCTF{I_h4te_th3s3_4dm1n5}</td></tr></table></html>'
            else:
                return '<html><h1>Bad Auth</h1></html>'
            #if the cookie is not the admin flag, return to login
        else:
            page = login_page()
            return page

@app.route('/todo', methods=['GET'])
def todo():
    return '''<html><h1>TODO</h1><p>1. Update the 'user' table data</p></html>'''
           

@app.route('/login', methods=['GET'])
def login():
    if request.remote_addr != '127.0.0.1' and request.remote_addr != 'localhost' and request.remote_addr != '2130706433' and request.remote_addr != '0.0.0.0':
        #return a 403 error and a message if the user is not on the local host and print their ip
        return 'You are not on the local host. Your IP is ' + request.remote_addr
    username = request.args.get('username')
    password = request.args.get('password')
    user_flag = getuser.get_flag(username, password)
    #set user_flag as the cookie and redirect to admin
    response = redirect('/admin?arg=' + str(user_flag), code=302)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)