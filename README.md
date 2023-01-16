# Py-FSM - Máquina de estados finitos para Python

Aplicante: João Victor Sawada [[E-mail](mailto:joaovictorsawada@gmail.com)] [[Github](https://github.com/nyvemm)]

### Sobre o projeto

O projeto consiste em uma máquina de estados finitos para Python, que permite a criação de máquinas de estados finitos de forma simples e intuitiva.

### Requerimentos

Para rodar o projeto, é necessário ter instalado:

- [Docker](https://www.docker.com/) - Para subir, rodar e testar a aplicação
- [Docker Compose](https://docs.docker.com/compose/) - Para criar e rodar os containers

### Tecnologias utilizadas

- [Poetry] - Gerenciador de pacotes e dependências para Python
- [Flask]- Framework web minimalista para Python
- [SQLAlchemy] - Biblioteca ORM para Python
- [Alembic] - Ferramenta para gerenciamento de migrações de banco de dados para SQLAlchemy
- [Python-dotenv] - Biblioteca para carregar variáveis de ambiente em Python
- [Flask-SQLAlchemy] - Extensão para facilitar o uso do SQLAlchemy com Flask
- [Flask-RESTx] - Extensão para adicionar o Swagger ao Flask
- [Flask-Caching] - Extensão para gerenciar cache em Flask
- [Unittest] - Biblioteca de testes unitários para Python
- [Psycopg2-binary] - Biblioteca para conectar-se a banco de dados PostgreSQL

### Como rodar o projeto

Antes de rodar o projeto, é necessário criar um arquivo `.env` na raiz do projeto, com as seguintes variáveis de ambiente ou simplesmente copiar o arquivo `.env.example` para `.env`:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=pyfsm

FLASK_APP=app:create_app
FLASK_DEBUG=1
DATABASE_URL=postgresql://postgres:postgres@db:5432/pyfsm
```

Para facilitar a execução dos comandos, foi criado um Makefile, que pode ser executado com o comando `make <comando>`, onde `<comando>` é o comando desejado. É possível ver a lista de todos os comandos no arquivo `Makefile`.

Para rodar o projeto, é necessário executar os seguintes comandos:

```bash
make up
```

Isso irá subir os containers necessários para rodar o projeto. Depois disso, é só abrir o navegador e acessar o endereço `http://localhost:8000/`.

### Como rodar os testes

Este projeto conta com testes unitários para garantir a qualidade do código. Para rodar os testes, é necessário executar o seguinte comando:

```bash
make test
```

Esse repositório também está integrado com o Github Actions, que executa os testes a cada push ou pull request. Para ver o resultado dos testes, é só acessar a aba `Actions` do repositório.

### Documentação

Foi utilizado o Swagger para documentar a API. Para acessar a documentação, é só acessar o endereço `http://localhost:8000/`.

Modelar uma máquina de estados finita usando classes (se você quiser), com
uma classe para os estados e outra para transições, além do relacionamento
entre elas. Você deve escrever "do zero" e não utilizar uma biblioteca (é simples,
prometo).

### Requisitos

O projeto era sobre criar uma máquina de estados finitos, que permite a criação de máquinas de estados finitos de forma simples e intuitiva. Para isso, foi criado um projeto em Python, utilizando Flask, SQLAlchemy e Alembic.

- [X] Criar uma máquina de estados finitos
- [X] Possibilitar a criação de estados
- [X] Possibilitar a listagem de estados
- [X] Possibilitar a criação de transições
- [X] Possibilitar a listagem de transições
- [X] Possibilitar de descobrir as possíveis transições de um estado
- [X] Possibilitar de descobrir a próxima transição de um estado
- [X] Usar váriaveis de ambiente
- [X] Usar Docker
- [X] Subir a aplicação em um servidor
- [X] Utilizar um banco de dados para persistir os dados
- [X] Utilizar uma política de cache
- [X] Documentar a API utilizando Swagger

### Deploy

O projeto foi deployado na Vercel, que é uma plataforma de hospedagem de sites estáticos e backend serverless. Para acessar o projeto, é só acessar o endereço: https://py-fsm.vercel.app/

---