
import sqlite3

import flask
from flask import Flask, redirect
from flask import render_template
from flask import request

import db_u

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



@app.route("/")
def enter():
    # Connecting to DB
    conn = sqlite3.connect('app.db_u')
    conn.row_factory = dict_factory
    c = conn.cursor()
    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('index.html')



@app.route('/registration', methods=['GET', 'POST'])
def registration():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        user = {}
        user['Firstname'] = request.form.get('Firstname')
        user['Lastname'] = request.form.get('Lastname')
        user['Username'] = request.form.get('Username')
        user['ObshagaAddress'] = request.form.get('ObshagaAddress')
        user['Room'] = request.form.get('Room')
        user['Password'] = request.form.get('Password')

        # save to database
        conn = sqlite3.connect('app.db_u')
        c = conn.cursor()

        c.execute("SELECT * FROM users where Username='%s'" % user['Username'])
        if c.fetchone():
            # user with this login is already in my database
            error_message = "user_exists"
        else:
            c.execute("INSERT INTO users "
                      "(Firstname, Lastname, Username, ObshagaAddress, Room, Password) "
                      "VALUES "
                      "('{Firstname}','{Lastname}','{Username}','{ObshagaAddress}','{Room}','{Password}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        return redirect('/user/%s/' % user['Username'])

    return render_template(
        "registr.html",
        user_created=user_created,
        error_message=error_message
    )



@app.route('/sign_in')
def sign_in():
    return render_template('sign in.html')



@app.route('/search')
def search():


    q = request.args.get('query')

    conn = sqlite3.connect('app.db_r')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM requests WHERE name LIKE '%{q}%' OR benefits LIKE '%{q}%'"
              "".format(q=q))
    requests = list(c.fetchall())

    # Close connection
    conn.close()

    return render_template('mainpage.html', q=q, requests=requests)



@app.route('/help')
def helping():
    return render_template('help.html')


@app.route('/addrequest', methods=['GET', 'POST'])
def add_request():

    request_created = False
    error_message = ""

    if request.method == 'POST':
        # add new request data
        request = {}
        request['name'] = request.form.get('name')
        request['condition'] = request.form.get('condition')
        request['benefits'] = request.form.get('benefits')
        request['ObshagaAddress'] = request.form.get('ObshagaAddress')
        request['time'] = request.form.get('time')

        # save to database
        conn = sqlite3.connect('app.db_r')
        c = conn.cursor()

        c.execute("SELECT * FROM requests where name='%s'" % request['name'])
        if c.fetchone():
            # request with this login is already in my database
            error_message = "request_exists"
        else:
            c.execute("INSERT INTO requests "
                      "(name, condition, benefits, ObshagaAddress, time) "
                      "VALUES "
                      "('{name}','{condition}','{benefits}','{ObshagaAddress}','{time}')"
                      "".format(**request))
            conn.commit()
            request_created = True
        conn.close()

    return render_template(
        "addrequest.html",
        request_created=request_created,
        error_message=error_message
    )

@app.route('/user/<username>')
def userpage(username):
    conn = sqlite3.connect('app.db_u')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users WHERE username='%s'" % username)
    user_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("userpage.html", user=user_data)



app.run()