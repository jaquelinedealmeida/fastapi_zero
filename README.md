#FASTAPI COM DUNOSSAURO - 2025#

## EM Desenvolvimento

### Comandos:

- entrar no ambiente virtual do poetry

`poetry shell` :

- Ver as configurações do poetry e caminho de interpretação do VSCode
  `poetry show fastapi`:

- Setar o caminho do Pyhton a ser utilizado no ambiente virtual
  `C:/Users/jaque/AppData/Local/pypoetry/Cache/virtualenvs/fastapi-zero-2ww5oAaX-py3.12/Scripts/activate`

- Executa o fastapi no ambiente virtual
  `poetry run fastapi dev fastapi_zero/app.py`

### Documentação executável (Swagger)

http://127.0.0.1:8000/docs

### Documentação não executável

http://127.0.0.1:8000/redoc

### Ferramentas:

#### Ruff: linter e formatador

- Instalação: `poetry add --group dev ruff`
- Verificar lint: `poetry run ruff check`
- Consertar erros: `poetry run ruff check --fix`
- Formatar os arquivos: `poetry run ruff format`

#### Pytest

- Verifica o que está sendo coberto pelo teste e o que não (cobertura de código)
  `poetry add --group dev pytest pytest-cov`

- Testes verboso (mais informações)
  `pytest --cov=fastapi_zero -vv`

- Ver a cobertura de testes em arquivo html:
  `coverage html`

- Taskipy: Para configurar comandos
  `poetry add --group dev taskipy`

- Ignora arquivos python no repositório(roda só uma vez)
  ` pipx run ignr -p python > .gitignore`

`poetry run task test`

## Para conexão em rede

## SQL Alchemy

`poetry add sqlalchemy`

### Breakpoint

Debugando no teste, use o comando abaixo para o terminal ficar interativo e usar o PDB.
`pytest -s`
Usar

- mapper
- connection
- target

## Configuração de ambientes

Possibilita o uso diferenciado de ambientes de desenvolvimento e produção para validações.
`poetry add pydantic-settings`
