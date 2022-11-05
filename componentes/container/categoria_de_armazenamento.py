from enum import Enum


class CategoriaDeArmazenamento(Enum):
    """
    Representação das possíveis categoriais de armazenamento existentes
    no ecosistema de dados
    """
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    SQL_SERVER = "sql_server"
