from fastapi import FastAPI
from http import HTTPStatus

from fastapi_zero.schemas import Message
from fastapi.responses import HTMLResponse

app = FastAPI(title='Minha API')


@app.get(
    '/', 
    status_code=HTTPStatus.OK,
    response_model=Message
)
def read_root():
    return {'message':'Hello, World'}

@app.get(
    '/html', 
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse
)
def read_html():
    return"""
     <html>
        <head>
        <title>Minha API</title>
        <body>
            <h1>Olá, mundo</h1>
        </body>
        </head>
     </html>
    """

