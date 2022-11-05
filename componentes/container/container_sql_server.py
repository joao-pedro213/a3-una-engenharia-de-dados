from typing import List

from pandas import DataFrame, Series
from dotenv import dotenv_values, find_dotenv
from pyodbc import connect as pyodbc_connect

from componentes.container.container import Container
from componentes.container.categoria_de_armazenamento import \
    CategoriaDeArmazenamento
from componentes.artefato.artefato import Artefato


class ContainerSQLServer(Container):
    """
    Representação do container sql server
    """
    def __init__(self) -> None:
        super().__init__(
            categoria_de_armazenamento=CategoriaDeArmazenamento.SQL_SERVER)

    def extrair_dados(self, artefato: Artefato) -> DataFrame:
        raise NotImplementedError()

    def persistir_dados(self, artefato: Artefato, dataframe: DataFrame) -> None:
        """
        Persiste o artefato informado como parâmetro no container sql server
        """
        try:
            conexao = pyodbc_connect(self._gerar_string_de_conexao())
            cursor = conexao.cursor()
            cursor.execute(f"delete from {artefato.nome}")
            for _, linha in dataframe.iterrows():
                comando = self._criar_comando_de_insercao(
                    tabela=artefato.nome,
                    colunas=dataframe.columns,
                    linha=linha)
                cursor.execute(comando)
            conexao.commit()
            cursor.close()
            conexao.close()
        except Exception as excessao:
            print(excessao)
            conexao.close()
            raise

    def _gerar_string_de_conexao(self) -> str:
        """
        Gera a string de conexão do sql server
        """
        segredos = {**dotenv_values(dotenv_path=find_dotenv())}
        return (
            f"DRIVER={{{segredos['DRIVER']}}};"
            + f"SERVER={segredos['SERVIDOR']};"
            + f"DATABASE={segredos['BANCO_DE_DADOS']};"
            + f"UID={segredos['USUARIO']};"
            + f"PWD={segredos['SENHA']};")

    def _criar_comando_de_insercao(
            self,
            tabela: str,
            colunas: List[str],
            linha: Series) -> str:
        """
        Cria um comando de insert baseado na tabela, listagem de linhas e
        colunas informadas como parametro
        """
        colunas = sorted(colunas)
        texto_colunas = "(" + ", ".join(colunas) + ")"
        valores = [str(linha[coluna]) for coluna in colunas]
        texto_valores = "('" + "', '".join(valores) + "')"
        return f"insert into {tabela} {texto_colunas} values {texto_valores}"
