def get_paic_silver_schema() -> dict:
    """
    Definição do schema dos arquivos paic silver
    """
    return {
        "ano_pesquisa": int,
        "variavel": str,
        "codigo_cnae": str,
        "categoria_empresa": str,
        "valor": int,
        "unidade": str,
        "pesquisa":str
    }
