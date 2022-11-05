from pandas import DataFrame

from componentes.container.container import Container
from componentes.artefato.artefato import Artefato
from componentes.logger.logger import Logger


class Pipeline:
    """
    Pipeline de dados responsável por realizar o processo de extração,
    transformação e carregamento a partir de uma referência de entreda e outra
    de saída
    """
    def __init__(
        self,
        artefato_de_entrada: Artefato,
        container_de_entrada: Container,
        artefato_de_saida: Artefato,
        container_de_saida: Container) -> None:
        self._artefato_de_entrada = artefato_de_entrada
        self._container_de_entrada = container_de_entrada
        self._artefato_de_saida = artefato_de_saida
        self._container_de_saida = container_de_saida
        self._logger = Logger()

    def executar_etl(self) -> None:
        """
        Responsável por orquestrar o processo de ETL
        """
        self._logger.log_mensagem(mensagem="Iniciando processo de ETL")
        dados = self._extrair_dados_da_fonte()
        dados_transformados = self._transformar_dados(dataframe=dados)
        self._carregar_dados(dataframe=dados_transformados)

    def _extrair_dados_da_fonte(self) -> DataFrame:
        """
        Lê o artefato de entrada em seu respectivo container
        """
        self._logger.log_mensagem(
            mensagem=f"Extraindo artefato: {str(self._artefato_de_entrada)}")
        return (
            self._container_de_entrada
            .extrair_dados(artefato=self._artefato_de_entrada))

    def _transformar_dados(self, dataframe: DataFrame) -> DataFrame:
        """
        Realiza a normalização e tratamento de dados do artefato
        de entrada
        """
        return dataframe

    def _carregar_dados(self, dataframe: DataFrame) -> None:
        """
        Persiste os dados no container de saída
        """
        self._logger.log_mensagem(
            mensagem=f"Carregando artefato: {str(self._artefato_de_saida)}")
        self._container_de_saida.persistir_dados(
            artefato=self._artefato_de_saida,
            dataframe=dataframe)
