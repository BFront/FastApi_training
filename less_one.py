from fastapi import FastAPI

app = FastAPI(
    title='First FAST API app',
    version='0.0.1'
)
fake_base = [
    {'id':1,'name':'Ivan', 'money':100},
    {'id':2,'name':'Petr', 'money':100},
    {'id':3,'name':'Nikola', 'money':100},
    {'id':4,'name':'Lida', 'money':100},
    {'id':5,'name':'Nina', 'money':100},
]

@app.get('/people/{user_id}')
def info_user(user_id: int):
    return [user for user in fake_base if user.get('id') == user_id]