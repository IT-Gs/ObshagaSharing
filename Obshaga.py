
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


    return render_template('mainpage.html')


@app.route('/help')
def helping():
    return render_template('help.html')

@app.route('/request/<requestname>')
def show_user_request(requestname):
    requestname= db_u.get_request(requestname)
    return render_template('show_user_request.html', requestname=requestname)

@app.route('/addrequest', methods=['GET', 'POST'])
def add_request():
    import sqlite3
    conn = sqlite3.connect('app.db')

    conn.close()
    return render_template('addrequest.html')

@app.route('/user/<username>')
def userpage(username):
    username = db_u.get_user(username),
    return render_template('userpage.html', username = username)






#seminar 20 nov

@app.route('/search1')
def search_for_person():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    q = flask.request.args.get('query')

    requests = db_u.get_requests_by_name(q)

    c.execute("SELECT * FROM request WHERE name LIKE '{}'".format(q))
    users = list(c.fetchall())

    c.close()
    return render_template('search_results.html', q=q, requests=requests)

@app.route('/search_page1')
def search1():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    q = ""

    c.execute("SELECT * FROM staff WHERE name LIKE '%s'" % q)
    users = list(c.fetchall())

    c.close()
    return render_template('page1.html', users=users)

app.run()