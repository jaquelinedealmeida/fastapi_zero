from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models import User, table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///memory')
    # cria todas as tabelas
    table_registry.metadata.create_all(engine)

    # interação com o banco de dados
    with Session(engine) as session:
        yield session  # abriu a sessão e depois dropa

    # deleta todas as tabelas
    table_registry.metadata.drop_all(engine)


# criar uma data fake para test
@contextmanager
def _mock_db_time(*model, time=datetime(2025, 5, 20)): #*exige que model seja usado
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time
        #print(target)
        #breakpoint()

    event.listen(User, 'before_insert', fake_time_hook)

    # retorna o tempo
    yield time

    event.remove(User, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
