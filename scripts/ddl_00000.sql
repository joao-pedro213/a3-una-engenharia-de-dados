create table dimensao_cnae (
    id_cnae int not null primary key,
    codigo varchar(max),
    descricao varchar(max),
    tipo varchar(max)
);

create table dimensao_variaveis_pesquisa (
    id_variavel int not null primary key,
    variavel varchar(max),
    pesquisa varchar(max),
    ano int
);

create table dimensao_unidade_resultado (
    id_unidade int not null primary key,
    nome varchar(max)
);

create table dimensao_categoria_empresa (
    id_categoria int not null primary key,
    nome varchar(max)
);

create table fato_resultado_pesquisa_paic (
    id_resultado int not null primary key,
    id_cnae int foreign key references dimensao_cnae(id_cnae),
    id_variavel int foreign key references dimensao_variaveis_pesquisa(id_variavel),
    id_unidade int foreign key references dimensao_unidade_resultado(id_unidade),
    id_categoria int foreign key references dimensao_categoria_empresa(id_categoria),
    valor int,
);