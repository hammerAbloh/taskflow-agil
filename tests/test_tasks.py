from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Sistema funcionando"}

def test_crud_tarefas():
    # 1. Listar tarefas inicial (vazia)
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert response.json() == []

    # 2. Criar uma tarefa com prioridade
    nova_tarefa = {
        "id": 0,
        "titulo": "Implementar prioridade",
        "prioridade": "Alta",
        "status": "Em Progresso"
    }
    response = client.post("/tarefas", json=nova_tarefa)
    assert response.status_code == 200
    assert response.json() == nova_tarefa

    # 3. Listar tarefas e ver se ela está lá
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["prioridade"] == "Alta"

    # 4. Editar a tarefa
    tarefa_editada = {
        "id": 0,
        "titulo": "Implementar prioridade",
        "prioridade": "Baixa",
        "status": "Concluído"
    }
    response = client.put("/tarefas/0", json=tarefa_editada)
    assert response.status_code == 200
    assert response.json() == tarefa_editada

    # 5. Deletar a tarefa
    response = client.delete("/tarefas/0")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Tarefa removida"}

    # 6. Listar novamente (vazia)
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert response.json() == []

def test_erros_tarefas_inexistentes():
    # Testar PUT em tarefa que não existe (deve retornar 404)
    tarefa_dados = {
        "id": 99,
        "titulo": "Tarefa Fantasma",
        "prioridade": "Média",
        "status": "A Fazer"
    }
    response = client.put("/tarefas/99", json=tarefa_dados)
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada"

    # Testar DELETE em tarefa que não existe (deve retornar 404)
    response = client.delete("/tarefas/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada"