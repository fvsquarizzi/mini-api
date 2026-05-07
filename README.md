# Mini API de Tarefas com FastAPI

Uma API simples de gerenciamento de tarefas desenvolvida com FastAPI para praticar conceitos fundamentais de APIs REST.

## Funcionalidades

* Criar tarefas
* Listar tarefas
* Deletar tarefas
* Validação com Pydantic
* IDs automáticos
* Armazenamento em memória
* Documentação automática com Swagger

## Tecnologias utilizadas

* Python
* FastAPI
* Pydantic
* Uvicorn

## Estrutura

```bash
.
├── main.py
└── model.py
```

## Endpoints

### GET `/`

Retorna o status da API.

### POST `/tasks`

Cria uma nova tarefa.

Exemplo de body:

```json
{
  "title": "Estudar FastAPI",
  "done": false
}
```

### GET `/tasks`

Lista todas as tarefas cadastradas.

### DELETE `/tasks/{task_id}`

Remove uma tarefa pelo ID.

## Como executar

```bash
docker compose up --build
```

## Documentação automática

Swagger:

```text
/docs
```

Redoc:

```text
/redoc
```

## Objetivo

Esse projeto foi criado para praticar:

* rotas HTTP
* schemas com Pydantic
* tipagem no Python
* tratamento de erros
* organização básica de APIs com FastAPI
