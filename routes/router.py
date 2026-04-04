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

def response(sucess: bool, data=None, message=""):
    return{
        "sucess": sucess,
        "data": data,
        "message": message
    }

@router.get("/")
def home():
    return response(True, {"status": "API Online"}, "Bem Vindo ao Gerenciador de Tarefas")

@router.get("/tarefas")
def listar_tarefas():
    tasks = manager.get_all_tasks()
    return response(True, tasks, "Lista de tarefas recuperada")

@router.get("/tarefas/{task_id}")
def get_task(task_id: int):
    task = manager.get_task_by_id(task_id)
    if not task:
        return JSONResponse(status_code=404, content=response(False, None, "Tarefa não encontrada"))
    return response(True, task, "Tarefa encontrada")

@router.post("/tarefas", status_code=201)
def create_task(task: TaskCreate):
    try:
        new_task = manager.create_task(task.title, task.desc)
        return response(True, new_task, "Tarefa criada com sucesso")
    except Exception as e:
        return JSONResponse(status_code=500, content=response(False, None, str(e)))

@router.delete("/tarefas/{task_id}")
def delete_task(task_id: int):
    if not manager.delete_task(task_id):
        return JSONResponse(status_code=404, content=response(False, None, "Tarefa não existe"))
    return response(True, None, "Tarefa removida com sucesso")

@router.patch("/tarefas/{task_id}/concluir")
def complete_task(task_id: int):
    if not manager.complete_task(task_id):
        return JSONResponse(status_code=404, content=response(False, None, "Erro ao concluir: Tarefa não encontrada"))
    return response(True, None, "Tarefa concluída")

@router.patch("/tarefas/{task_id}/reabrir")
def reopen_task(task_id: int):
    if not manager.reopen_task(task_id):
        return JSONResponse(status_code=404, content=response(False, None, "Erro ao reabrir: Tarefa não encontrada"))
    return response(True, None, "Tarefa reaberta")

@router.get("/tarefas/buscar/")
def search_tasks(title: str):
    results = manager.search_tasks(title)
    if not results:
        return response(True, [], "Nenhuma tarefa corresponde à busca")
    return response(True, results, f"Resultados para: {title}")