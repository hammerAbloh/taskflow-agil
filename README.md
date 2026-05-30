# TaskFlow Agile

Sistema simples de gerenciamento de tarefas utilizando FastAPI e metodologias ágeis.

## Funcionalidades

- Criar tarefas
- Editar tarefas
- Excluir tarefas
- Listar tarefas
- Prioridade de tarefas

## Tecnologias

- Python
- FastAPI
- Pytest
- GitHub Actions

## Como executar

```bash
uvicorn src.main:app --reload
```

## Rodar testes

```bash
pytest
```

## Estrutura do Repositório

- `/src`: Contém o código-fonte da aplicação FastAPI.
- `/tests`: Contém a suite de testes automatizados com Pytest.
- `/docs`: Contém a documentação com diagramas de classes e de casos de uso em formato UML/Mermaid.
- `/github/workflows`: Contém a configuração de Integração Contínua (CI) do GitHub Actions.

## Metodologia Ágil

Foi utilizado o framework Kanban integrado ao GitHub Projects para a divisão e monitoramento das entregas em tempo real ("A Fazer", "Em Progresso" e "Concluído").

## Gestão de Mudanças

* **Justificativa da Alteração de Escopo:** Durante a fase de planejamento inicial com a startup de logística (cliente fictício), identificou-se a necessidade urgente de categorizar tarefas por prioridade. Isso permite que a equipe foque nos entregáveis críticos de forma eficiente. O Kanban foi adaptado dinamicamente com novos cartões e o campo `prioridade` foi implementado no modelo de dados das tarefas.

## Status do Projeto

O projeto foi concluído com sucesso. Todos os testes unitários e de integração estão passando (100% de cobertura funcional).