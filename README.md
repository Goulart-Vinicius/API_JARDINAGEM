# API de Jardinagem

## Sobre

A API de Jardinagem está sendo desenvolvida como um trabalho da matéria de Programação para Engenharias no curso de Engenharia da Computação. O objetivo do projeto é criar uma aplicação prática que possa ser utilizada no dia a dia, focando no gerenciamento de serviços de jardinagem. A API utiliza FastAPI para a construção do backend, Peewee ORM para a interação com o banco de dados SQLite, e segue a arquitetura MVC (Model-View-Controller) com modularização de arquivos e Programação Orientada a Objetos (POO) para facilitar o desenvolvimento, compreensão e expansão do projeto.

## Funcionalidades

### User
- Cadastrar, deletar, selecionar e alterar informações de funcionários.

### Funcionário
- Cadastrar, alterar, visualizar e deletar seus serviços.
- Visualizar sua agenda.
- Ver serviços solicitados em uma tabela.

### Cliente
- Visualizar serviços de vários funcionários.
- Solicitar serviços de jardinagem.


## Estrutura do Projeto
- **controller/**: Contém os controladores para gerenciar a lógica de negócios.
- **model/**: Contém os modelos de dados usando Peewee ORM.
- **router/**: Contém as rotas para o FastAPI.
- **app.py**: Arquivo principal para executar a aplicação.
- **banco.db**: Banco de dados SQLite.
- **migrate.py**: Script para migração de dados.

## Rotas da API

### Usuários
- `GET /users/{user_id}`: Obtém um usuário pelo ID.
- `POST /users/`: Adiciona um novo usuário.
- `PUT /users/{user_id}`: Atualiza um usuário pelo ID.
- `DELETE /users/{user_id}`: Desativa um usuário pelo ID.

### Serviços
- `GET /services/{service_id}`: Obtém todos os serviços.
- `GET /services/{service_id}`: Obtém um serviço pelo ID. (Não implementado)
- `POST /services/`: Adiciona um novo serviço. (Não implementado)
- `PUT /services/{service_id}`: Atualiza um serviço pelo ID. (Não implementado)
- `DELETE /services/{service_id}`: Deleta um serviço pelo ID. (Não implementado)


## Como Executar

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute o arquivo `app.py` com `uvicorn app:app --reload`.
4. Acesse a API via `http://127.0.0.1:8000`.

## Tecnologias Utilizadas

- FastAPI
- Peewee ORM
- SQLite

## Próximos Passos
- Implementar testes unitários.
- Melhorar a documentação.
- Adicionar mais funcionalidades conforme o feedback dos usuários.
