from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append('/mnt/1962bfc0-f9ca-4c35-a3e2-7f1d23b699bd/PROGRAMAS/Cursos/Python/Estudos/03-26/14-03-26')
from manager import TaskManager

class TaskRequest(BaseModel):
    title: str
    desc: Optional[str] = ""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = TaskManager()

@app.get("/")
def home():
    return {"status": "API Online", "sistema": "Gerenciador de Tarefas"}

@app.get("/tarefas")
def listar_tarefas_api():
    manager.task_list = manager.load_task()
    return manager.task_list

@app.get("/tarefas/{id}")
def listtask_fromid(id: str):
    tarefas = manager.load_task()
    tarefa_encontrada = next((task for task in tarefas if task["ID"] == id), None)
    if not tarefa_encontrada:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_encontrada

@app.post("/tarefas", status_code=201)
async def create_task(task_data: TaskRequest):
    try:
        manager.new_task(task_data.title, task_data.desc)
        return {"message": "Tarefa criada!", "all_tasks": manager.task_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))