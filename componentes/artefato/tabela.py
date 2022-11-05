from dataclasses import dataclass

from componentes.artefato.artefato import Artefato


@dataclass
class Tabela(Artefato):
    """
    Representação de uma tabela localizada em um banco de dados
    """
    banco_de_dados: str
    schema: str = "dbo"

    def __str__(self) -> str:
        return f"{self.banco_de_dados}.{self.schema}.{self.nome}"
