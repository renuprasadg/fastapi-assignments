from fastapi import APIRouter, HTTPException
from app.data import sample_data

router = APIRouter()

@router.get("/servers")
def get_servers(environment: str|None = None, 
                  application: str|None = None, 
                  status: str|None = None
    ):
    result = sample_data.servers

    if environment:
        result = [
            server
            for server in result
            if server["environment"].lower() == environment.lower()
        ]
    if status:
        result = [
            server
            for server in result
            if server["status"].lower() == status.lower()
        ]        
    if application:
        result = [
            server
            for server in result
            if server["application"] == application.lower()
        ]         
    return {
        "count": len(result),
        "servers": result
    } 

@router.get("/servers/{server_id}")
def get_server_by_id(server_id: int):
    for server in sample_data.servers:
        if server_id == server['id']:
            return server
    raise HTTPException( 
        status_code=404, 
        detail="server is not found" 
    )     