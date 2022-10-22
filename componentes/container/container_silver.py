from pandas import DataFrame, read_csv

from componentes.container.container import Container
from componentes.container.categoria_de_armazenamento import \
    CategoriaDeArmazenamento
from componentes.artefato.artefato import Artefato


class ContainerSilver(Container):
    """
    Representação do container silver
    """
    def __init__(self) -> None:
        super().__init__(
            categoria_de_armazenamento=CategoriaDeArmazenamento.SILVER)

    def extrair_dados(self, artefato: Artefato) -> DataFrame:
        """
        Lê dados do artefato armazenado no container bronze
        """
        self.validar_artefato(artefato=artefato)
        return read_csv(
            filepath_or_buffer=str(artefato),
            sep=";",
            dtype=artefato.schema)

    def persistir_dados(self, artefato: Artefato, dataframe: DataFrame) -> None:
        """
        Persiste o artefato informado como parâmetro no container silver
        """
        self.validar_artefato(artefato=artefato)
        dataframe.to_csv(
            path_or_buf=str(artefato),
            sep=";",
            mode="w",
            index=False,
            encoding="utf-8")
