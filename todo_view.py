from flask import Blueprint, render_template, request, redirect, session
from todo_dao import find_all, save, finish, delete

todos_app = Blueprint('todos_app', __name__)

@todos_app.route('/')
def index():
    todos = find_all()
    return render_template("list.html", todos=todos)

@todos_app.route('/write', methods=['POST'])
def todo_write():
  username = session.get('username')
  if username == None:
    return redirect("/")
  title = request.form.get('title')
  save(title, username)
  return redirect("/")

@todos_app.route('/finish', methods=['POST'])
def todo_toggle():
  username = session.get('username')
  if username == None:
    return redirect("/")
  tno = int(request.form.get('tno'))
  finish(tno, username)
  return redirect("/")

@todos_app.route('/delete', methods=['POST'])
def todo_delete():
  username = session.get('username')
  if username == None:
    return redirect("/")
  tno = int(request.form.get('tno'))
  delete(tno, username)
  return redirect("/")