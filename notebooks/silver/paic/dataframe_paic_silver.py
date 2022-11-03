from os import listdir, path as os_path
from typing import List

from pandas import DataFrame, concat

from componentes.artefato.arquivo import Arquivo
from componentes.container.categoria_de_armazenamento import \
    CategoriaDeArmazenamento
from componentes.container.container_silver import ContainerSilver
from notebooks.silver.paic.schema.paic_schema import get_paic_silver_schema


class DataFramePAICSilver:
    """
    Ferramenta para gerar a representação da tabela PAIC unificada
    em sua categoria silver
    """
    def criar_dataframe(self) -> DataFrame:
        """
        Cria a tabela PAIC unificada em sua categoria silver
        """
        dataframes = []
        arquivos_paic_silver = self._criar_lista_de_arquivos_paic_silver()
        for arquivo in arquivos_paic_silver:
            dataframe = ContainerSilver().extrair_dados(artefato=arquivo)
            dataframe["pesquisa"] = arquivo.nome
            dataframes.append(dataframe)
        return concat(objs=dataframes)

    def _criar_lista_de_arquivos_paic_silver(self) -> List[Arquivo]:
        """
        Gera a listagem de arquivos PAIC armazenados no container silver
        """
        arquivos = []
        nome_dos_arquivos = listdir(path="../../../dados/silver/paic")
        for nome_arquivo in nome_dos_arquivos:
            arquivo = Arquivo(
                nome=os_path.splitext(p=nome_arquivo)[0],
                categoria_de_armazenamento=CategoriaDeArmazenamento.SILVER,
                fonte="paic",
                schema=get_paic_silver_schema())
            arquivos.append(arquivo)
        return arquivos
