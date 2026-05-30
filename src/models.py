from pydantic import BaseModel

class Task(BaseModel):
    id: int
    titulo: str
    prioridade: str
    status: str
