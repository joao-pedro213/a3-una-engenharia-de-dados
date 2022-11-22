# A3 UC ENGENHARIA DE DADOS UNA

## Sobre o projeto

Este repositório contempla os artefatos produzidos para resolver o enunciado proposto no trabalho final da unidade curricular de Engenharia de Dados da universidade UNA realizado no último semestre de 2022.

### Objetivos

- Extração dos dados utilizando ferramentas do IBGE
- Exploração
- Tratamento
- Validação
- Analise
- Modelagem
- Criação de dashboards

### Dados utilizados

Os dados se tratam da pesquisa anual da indústria da construção (PAIC), que tem por
objetivo identificar as características estruturais básicas da atividade de construção no país e suas transformações no tempo, através de levantamentos anuais de dados econômico-financeiros segundo a classificação nacional de atividades econômicas (CNAE).

### Fonte
Sistema IBGE de Recuperação Automática (SIDRA)

### Configurando o projeto

#### Instalando dependências
```
pip install -r requirements.txt 
```
#### Criando variáveis de ambiente
Criar um arquivo nomeado .env na raiz do projeto e preencher as seguintes variáveis:
```
DRIVER="ODBC Driver 13 for SQL Server"
SERVIDOR="Nome do servidor do banco de dados"
BANCO_DE_DADOS="Nome do banco de dados"
USUARIO="Usuário do banco de dados"
SENHA="Senha para acesso ao banco de dados"
```