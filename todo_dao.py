import datetime as dt

# 할 일 목록
todos = []
# 할 일 번호
tno = 0

def save(title: str, username:str) -> dict:
  global tno
  tno += 1
  now = dt.datetime.now()
  formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
  todo = {'tno': tno, 'title': title, 'writeday': formatted_time, 'finish': False, 'writer':username}
  todos.append(todo)
  return todo

def find_all() -> list:
  return todos

def finish(tno: int, username:str) -> bool:
  for todo in todos:
    if todo['tno'] == tno and todo['writer']== username:
      todo['finish'] = True
      return True
  return False

def delete(tno: int, username:str) -> bool:
  for todo in todos:
    if todo['tno'] == tno and todo['writer']== username:
      todos.remove(todo)
      return True
  return False