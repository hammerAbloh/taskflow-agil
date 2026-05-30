from fastapi import APIRouter

router = APIRouter()

tarefas = []

@router.get("/")
def home():
    return {"mensagem": "Sistema funcionando"}

@router.get("/tarefas")
def listar_tarefas():
    return tarefas

@router.post("/tarefas")
def criar_tarefa(tarefa: dict):
    tarefas.append(tarefa)
    return tarefa

@router.put("/tarefas/{id}")
def editar_tarefa(id: int, tarefa: dict):
    tarefas[id] = tarefa
    return tarefa

@router.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    tarefas.pop(id)
    return {"mensagem": "Tarefa removida"}