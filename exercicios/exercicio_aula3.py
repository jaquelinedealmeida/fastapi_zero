from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title='Minha API')


@app.get('/users/{id}', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_users(id: int):
    users = ['user1', 'user2', 'user3']
    return {'id': id, 'users': users}


def read_html():
    return """
     <html>
        <head>
        <title>Meus Usuários</title>
        </head>
         <body>
            <h1>Users</h1>
        </body>
     </html>
    """
