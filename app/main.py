from fastapi import FastAPI
from app.routes import employees, servers

app = FastAPI()

app.include_router(employees.router)
app.include_router(servers.router)