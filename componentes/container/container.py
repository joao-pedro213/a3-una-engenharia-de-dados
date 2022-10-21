from abc import ABC, abstractmethod

from pandas import DataFrame

from componentes.container.categoria_de_armazenamento import \
    CategoriaDeArmazenamento
from componentes.artefato.artefato import Artefato


class Container(ABC):
    """
    Representação de um repositório para armazenamento e controle de dados
    """
    def __init__(
        self,
        categoria_de_armazenamento: CategoriaDeArmazenamento) -> None:
        self._categoria_de_armazenamento = categoria_de_armazenamento

    @abstractmethod
    def extrair_dados(self, artefato: Artefato) -> DataFrame:
        """
        Lê dados do artefato informado como parâmetro
        """

    def validar_artefato(self, artefato: Artefato) -> None:
        """
        Valida se a categoria de armazenamento do artefato informado
        como parâmetro é compátivel com o do container de referência
        """
        if (artefato.categoria_de_armazenamento !=
                self._categoria_de_armazenamento):
            mensagem_de_erro = (
                "A categoria de armazenamento do artefato "
                + f"({artefato.categoria_de_armazenamento.value}) é "
                + "incompatível com a do Container "
                + f"({self._categoria_de_armazenamento.value})")
            raise TypeError(mensagem_de_erro)

    @abstractmethod
    def persistir_dados(self, artefato: Artefato, dataframe: DataFrame) -> None:
        """
        Persiste o artefato informado como parâmetro no container de referência
        """
