create view pesquisa_paic as (
    select
        fato.id_resultado,
        dim_ce.nome as categoria_empresa,
        dim_vp.pesquisa,
        dim_vp.ano,
        dim_vp.variavel,
        dim_cnae.codigo as codigo_cnae,
        dim_cnae.descricao as descricao_cnae,
        dim_cnae.tipo as tipo_cnae,
        fato.valor,
        dim_ur.nome as unidade_valor
    from
        fato_resultado_pesquisa_paic fato
    inner join
        dimensao_categoria_empresa dim_ce
    on
        fato.id_categoria = dim_ce.id_categoria
    inner join
        dimensao_cnae dim_cnae
    on
        fato.id_cnae = dim_cnae.id_cnae
    inner join
        dimensao_variaveis_pesquisa dim_vp
    on
        fato.id_variavel = dim_vp.id_variavel
    inner
        join dimensao_unidade_resultado dim_ur
    on
        fato.id_unidade = dim_ur.id_unidade
);

create view total_de_receitas_por_grupo_de_atividade as (
    select
        descricao_cnae,
        ano,
        sum(valor) as valor
    from
        pesquisa_paic
    where
        tipo_cnae = 'Grupo'
        and pesquisa = 'estrutura_das_receitas'
        and variavel like 'Receita líquida'
    group by
        descricao_cnae, ano
);

create view total_de_despesas_por_grupo_de_atividade as (
    select
        descricao_cnae,
        ano,
        sum(valor) as valor
    from
        pesquisa_paic
    where
        tipo_cnae = 'Grupo'
        and pesquisa = 'estrutura_das_despesas'
        and variavel like 'Total de custos e despesas'
    group by
        descricao_cnae, ano
)