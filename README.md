Uma API REST assíncrona para gerenciamento de blogs pessoais, construída com FastAPI e MySQL.

## 📋 Descrição

Esta API permite criar, ler, atualizar e excluir posts de blog, com sistema de autenticação JWT. Desenvolvida para ser escalável e fácil de usar, com documentação automática via Swagger UI.

## ✨ Funcionalidades

- **Autenticação JWT**: Sistema seguro de login e autorização
- **Gerenciamento de Posts**:
  - Criar novos posts
  - Listar posts com filtros (publicado/não publicado, paginação)
  - Buscar post por ID
  - Atualizar posts existentes
  - Excluir posts
- **Validação de Dados**: Usando Pydantic para validação robusta
- **Documentação Interativa**: Swagger UI e ReDoc
- **Banco de Dados**: Suporte a MySQL com SQLAlchemy e databases
- **Testes**: Suite de testes com Pytest

## 🛠️ Tecnologias Utilizadas

- **Backend**: FastAPI
- **Banco de Dados**: MySQL
- **ORM**: SQLAlchemy
- **Autenticação**: PyJWT
- **Validação**: Pydantic
- **Servidor ASGI**: Uvicorn
- **Gerenciamento de Dependências**: Poetry
- **Testes**: Pytest + pytest-asyncio + httpx
- **Migrações**: Alembic


## 📚 Endpoints da API

### Autenticação

- `POST /auth/login` - Login de usuário

### Posts

- `GET /posts/` - Listar posts (com filtros: published, limit, skip)
- `POST /posts/` - Criar novo post
- `GET /posts/{id}` - Buscar post por ID
- `PATCH /posts/{id}` - Atualizar post
- `DELETE /posts/{id}` - Excluir post

## 📁 Estrutura do Projeto

```
fastapi-blog-api/
├── src/
│   ├── controllers/     # Rotas da API
│   ├── model/          # Modelos do banco de dados
│   ├── schemas/        # Schemas Pydantic
│   ├── Service/        # Lógica de negócio
│   ├── views/          # Modelos de resposta
│   ├── database.py     # Configuração do banco
│   ├── exceptions.py   # Exceções customizadas
│   ├── main.py         # Aplicação FastAPI
│   └── security.py     # Utilitários de segurança
├── tests/              # Testes
├── migration/          # Migrações do banco
├── pyproject.toml      # Configuração Poetry
├── alembic.ini         # Configuração Alembic
└── README.md
```

## 📞 Contato

Cleyton - [cleyton.p2025@gmail.com](mailto:cleyton.p2025@gmail.com)
telefone: +55 81 9 98863-4396
