CREATE TABLE dimensao_cnae (
    id_cnae int NOT NULL IDENTITY(1,1) PRIMARY KEY,
    codigo varchar(max),
    descricao varchar(max),
    tipo_cnae varchar(max),
);

CREATE TABLE dimensao_unidade_resultado (
    id_unidade int NOT NULL IDENTITY(1,1) PRIMARY KEY,
    nome varchar(max),
);

CREATE TABLE dimensao_categoria_empresa (
    id_categoria int NOT NULL IDENTITY(1,1) PRIMARY KEY,
    nome varchar(max),
);

CREATE TABLE dimensao_variaveis_pesquisa (
    id_variavel int NOT NULL IDENTITY(1,1) PRIMARY KEY,
    variavel varchar(max),
	ano int,
);

CREATE TABLE fato_resultado_pesquisa_paic (
	id_resultado int NOT NULL IDENTITY(1,1) PRIMARY KEY,
    id_cnae int FOREIGN KEY REFERENCES dimensao_cnae(id_cnae),
	id_variavel int FOREIGN KEY REFERENCES dimensao_variaveis_pesquisa(id_variavel),
	id_unidade int FOREIGN KEY REFERENCES dimensao_unidade_resultado(id_unidade),
	id_categoria int FOREIGN KEY REFERENCES dimensao_categoria_empresa(id_categoria),
	valor int,
);