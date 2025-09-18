from dataclasses import asdict
from datetime import datetime

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User, time=datetime.now()) as time:
        new_user = User(username='test', email='test@test', password='secret')

        session.add(new_user)  # faz somente uma operação ao adiconar um user
        session.commit()  # ao realizar o teste, o user será sempre deletado
        #e retornaá com o mesmo id

        # pedir o resultado da operação - scalar é um conceito de algebra.
        # tudo que vem do db covnerte em objeto python
        # faz abstração da querie
        user = session.scalar(select(User).where(User.username == 'test'))
    # breakpoint()

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test',
        'password': 'secret',
        'created_at': time,
    }
