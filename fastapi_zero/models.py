from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    """"
        Usando o init=False indica que o BD irá gerenciar a linha,
        criando ele mesmo.
        server_default indica que a hora usada será a  banco de dados.
        uniqque indica que será um dado único, não tendo repetição
    """
    id: Mapped[int] = mapped_column(
        init=False, primary_key=True
    )  # id gerenciado pelo banco de dados
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
