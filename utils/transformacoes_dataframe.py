"""
A proposta deste modulo é promover uma série de ferramentas para
performar transformações genéricas em um DataFrame Pandas
"""
from pandas import DataFrame

from componentes.logger.logger import Logger


def remover_espacamento_das_colunas(dataframe: DataFrame) -> DataFrame:
    """
    Remove espaçamentos a esquerda e a direita de todas as colunas
    """
    logger = Logger()
    logger.log_mensagem(mensagem="Removendo espaçamento das colunas")
    colunas = dataframe.columns
    for coluna in colunas:
        if dataframe[coluna].dtype == "str":
            dataframe[coluna] = dataframe[coluna].str.strip()
    return dataframe
