from fastapi import APIRouter, HTTPException
from src.models import Task

router = APIRouter()

tarefas = []

@router.get("/")
def home():
    return {"mensagem": "Sistema funcionando"}

@router.get("/tarefas")
def listar_tarefas():
    return tarefas

@router.post("/tarefas")
def criar_tarefa(tarefa: Task):
    tarefas.append(tarefa)
    return tarefa

@router.put("/tarefas/{id}")
def editar_tarefa(id: int, tarefa: Task):
    if id < 0 or id >= len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefas[id] = tarefa
    return tarefa

@router.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    if id < 0 or id >= len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefas.pop(id)
    return {"mensagem": "Tarefa removida"}