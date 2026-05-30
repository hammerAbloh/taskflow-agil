from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = 0
    titulo: str
    prioridade: str
    status: Optional[str] = "Pendente"

