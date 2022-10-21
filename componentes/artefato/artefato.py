from dataclasses import dataclass

from componentes.container.categoria_de_armazenamento import \
    CategoriaDeArmazenamento


@dataclass
class Artefato:
    """
    Representação de um artefato de dados que compõe o ecossistema
    """
    nome: str
    categoria_de_armazenamento: CategoriaDeArmazenamento
