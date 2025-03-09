from flask import Flask,session, redirect
from todo_view import todos_app

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

# 블루프린트 등록
app.register_blueprint(todos_app)

# @app.before_request
# def set_login():
#   session['username'] = 'summer'

@app.route("/spring")
def set_login_spring():
  session['username'] = 'spring'
  return redirect("/")

@app.route("/summer")
def set_login_summer():
  session['username'] = 'summer'
  return redirect("/")

@app.route("/logout")
def set_login_logout():
  session.clear()
  return redirect("/")

with app.test_request_context():
  print(app.url_map)

app.run(debug=True)