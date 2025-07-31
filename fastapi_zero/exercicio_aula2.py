from fastapi import FastAPI
from http import HTTPStatus

from fastapi.responses import HTMLResponse

app = FastAPI(title='Minha API')

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

