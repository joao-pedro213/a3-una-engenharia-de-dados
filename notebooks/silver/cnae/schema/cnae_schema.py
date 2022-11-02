def get_cnae_silver_schema() -> dict:
    """
    Definição do schema dos arquivos paic silver
    """
    return {
        "codigo_cnae": str,
        "denominacao": str,
        "tipo_cnae": str
    }
