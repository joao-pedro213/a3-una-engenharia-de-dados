"""
A proposta deste modulo é promover uma série de ferramentas para
gerar gráficos relevantes para o entimento da qualidade dos dados de maneira
generica
"""
from typing import List

from plotly.express import pie
from plotly.graph_objects import Table, Figure, Indicator
from pandas import DataFrame


def gerar_indicador_totalizacao_de_linhas(dataframe: DataFrame) -> None:
    """
    Gera um indicador com a totalização de linhas do DataFrame
    """
    figura = Figure()
    figura.add_trace(Indicator(value=dataframe.shape[0]))
    figura.update_layout(width=300, height=200, title="Total de linhas")
    figura.show()


def gerar_tabela_relacao_de_nulos_por_coluna(dataframe: DataFrame) -> None:
    """
    Gera uma tabela com a totalização de dados nulos por coluna do DataFrame
    """
    total_de_nulos_por_colunas = (
        dataframe
        .isnull()
        .sum()
        .to_frame(name="total_de_nulos")
        .reset_index()
        .rename(columns={"index": "colunas"}))
    tabela = Table(
        header=dict(values=["colunas", "total_de_nulos"]),
        cells=dict(values=[
            total_de_nulos_por_colunas.colunas,
            total_de_nulos_por_colunas.total_de_nulos]))
    figura = Figure(data=[tabela])
    figura.update_layout(
        width=600,
        height=400,
        title="Total de valores nulos por coluna")
    figura.show()


def gerar_tabela_relacao_de_linhas_duplicadas(
        dataframe: DataFrame,
        colunas: List[str]) -> None:
    """
    Gera um gráfico de pizza com a relação de linhas duplicadas no DataFrame
    de acordo com a listagem de colunas selecionadas para validação
    """
    dataframe["linha_duplicada"] = (dataframe.duplicated(subset=colunas))
    relacao_de_duplicidade = (
        dataframe
        .groupby(by=["linha_duplicada"])["linha_duplicada"]
        .count()
        .to_frame(name="count")
        .reset_index()
        .replace(
            to_replace={
                "linha_duplicada": {
                    False: "Não é duplicado",
                    True: "É duplicado"
                }
            }))
    grafico = pie(
        data_frame=relacao_de_duplicidade,
        values="count",
        names="linha_duplicada",
        width=600,
        height=400,
        hole=0.3,
        title="Relação de linhas duplicadas")
    grafico.update_traces(textposition="inside")
    grafico.show()
