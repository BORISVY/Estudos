from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from app.services.task_service import TaskManager

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    desc: Optional[str] = Field(default="", max_length=100)

router = APIRouter()
manager = TaskManager()

@router.get("/")
def home():
    return {"status": "API Online", "sistema": "Gerenciador de Tarefas"}

@router.get("/tarefas")
def listar_tarefas():
    return manager.get_all_tasks()

@router.get("/tarefas/{task_id}")
def get_task(task_id: int):
    task = manager.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@router.post("/tarefas", status_code=201)
def create_task(task: TaskCreate):
    try:
        manager.create_task(task.title, task.desc)
        return {"message": "Tarefa criada!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/tarefas/{task_id}")
def delete_task(task_id: int):
    deleted = manager.delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"message": "Tarefa removida com sucesso"}

@router.patch("/tarefas/{task_id}/concluir")
def complete_task(task_id: int):
    updated = manager.complete_task(task_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"message": "Tarefa concluída"}

@router.patch("/tarefas/{task_id}/reabrir")
def reopen_task(task_id: int):
    updated = manager.reopen_task(task_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"message": "Tarefa reaberta"}

@router.get("/tarefas/buscar/")
def search_tasks(title: str):
    results = manager.search_tasks(title)

    if not results:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada")

    return results

@router.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"Erro capturado: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "message": "Um problema no servidor foi detectado",
            "details": str(exc),
            "type": "Erro Interno"
        }
    )