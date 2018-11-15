from flask import Flask
app = Flask(_name_)

@app.route("/")
def enter():
  return "Enter"
#Первая страница для входа на сайт

@app.route('/registraion')
def registration():
  return "Register"
#Вторая страница для регистрации, если не зареган

@app.route("/search_page")
def search():
  return "main page"
#Третья страница, главная со списком просьб, поисковиком, и слева профиль с откликами на просьбы вошедшего юзера

@app.route('/help')
def help():
  return "help"
#Четвертая страница - написать отклик на просьбу, окно с вводом для отклика

@app.route('/help_outcome')
def help_outcome():
  return "your response sent :)"
#Пятая - окошко, где написано, что отклик отправлен пользователю (в принципе не очень нужна, просто для красоты)

@app.route('/your_request/<requestname>')
def show_user_request(requestname):
  return "Request %s" % requestname
#Шестая - список откликов на просьбу юзера, где можно принять или отклонить отклики

@app.route('/you_took_help')
def you_took_help():
  return "you_took_help :)"
#Седьмая - окошко, где написано, что "Позравляем! Вы приняли помощь от ..." (в принципе не очень нужна, просто для красоты)

@app.route('/add_request')
def add_request():
  return "input your request"
#Восьмое - введение просьбы

@app.route('/you_publish_request')
def publish_request():
  return "Congratulations! You publish request! :)"
#Девятое - окошко, где написано, что "Позравляем! Вы опубликовали просьбу, ждите откликов!" (в принципе не очень нужна, просто для красоты)

@app.route('/user/<username>')
def show_user_profile(username):
  return 'User %s' % username
#Десятая - страничка пользователя, слева просьбы пользователя, справа (пока предположительно просьбы, на которые отозвались с отзывами)

app.run(port=5000)
