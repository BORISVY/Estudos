from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.router import router as task_router

app = FastAPI()

# O middleware fica na instância principal do app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluímos as rotas que foram criadas no router.py
app.include_router(task_router)