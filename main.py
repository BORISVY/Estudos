from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes.router import router as task_router

app = FastAPI()
app.include_router(task_router)

# O middleware fica na instância principal do app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluímos as rotas que foram criadas no router.py
app.include_router(task_router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"success": False, "data": None, "message": "Erro interno detectado"}
    )