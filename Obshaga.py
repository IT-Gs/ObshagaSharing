from flask import Flask
from flask import render_template
import db
app = Flask(__name__)

@app.route("/")
def enter():
  return render_template('index.html')

@app.route('/registraion')
def registration():
  return render_template('registr.html')

@app.route('/search_page')
def search():
  return "main page"

@app.route('/help')
def help():
  return "help"


@app.route('/help_outcome')
def help_outcome():
  return "your response sent :)"

@app.route('/your_request/<requestname>')
def show_user_request(requestname):
  return render_template('show_user_request.html', requestname=requestname)


@app.route('/you_took_help')
def you_took_help():
  return "you_took_help :)"

@app.route('/add_request')
def add_request():
  return "input your request"


@app.route('/you_publish_request')
def publish_request():
  return "Congratulations! You publish request! :)"

@app.route('/user/<username>')
def show_user_profile(username):
  return 'User %s' % username

app.run(port=5000)