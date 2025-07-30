#FASTAPI COM DUNOSSAURO - 2025#

### Comandos:

`poetry shell` :

- entrar no ambiente virtual do poetry

`poetry show fastapi`:

- para ver as configurações do poetry e caminho de interpretação do VSCode

`poetry run fastapi dev fastapi_zero/app.py`

- Executa o fastapi no ambiente virtual

### Documentação executável (Swagger)

http://127.0.0.1:8000/docs

### Documentação não executável

http://127.0.0.1:8000/redoc

### Ferramentas:

- Ruff: linter e formatador
  `poetry add --group dev ruff`: Instalar
  `poetry run ruff check .`: Verificar lint
  `poetry run ruff format .`: Formatar os arquivos

- Pytest: testes
  `poetry add --group dev pytest pytest-cov`: Com o pytest-cov verifica o que está sendo coberto pelo teste e o que não (cobertura de código)
  `pytest --cov=fastapi_zero -vv` (v- verboso)
  `coverage html`: ver a cobertura de testes em arquivo html

- Taskipy: Para configurar comandos
  `poetry add --group dev taskipy`

- Ignora arquivos python no repositório(roda só uma vez)
  ` pipx run ignr -p python > .gitignore`
