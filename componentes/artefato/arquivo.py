from dataclasses import dataclass

from componentes.artefato.artefato import Artefato


@dataclass
class Arquivo(Artefato):
    """
    Representação de um arquivo que armazena dados
    """
    fonte: str
    schema: dict = None
    diretorio_raiz: str = "../../../dados"
    tipo: str = "csv"

    def __str__(self) -> str:
        return (
            f"{self.diretorio_raiz}/"
            + f"{self.categoria_de_armazenamento.value}/"
            + f"{self.fonte}/"
            + f"{self.nome}.{self.tipo}")
