from fastapi import APIRouter, HTTPException
from models.execution_request import Req
from utils.executor import run

r = APIRouter()

@r.post("/execute_code")
async def exec_code(req: Req):
    try:
        out, err = run(req.code)
        if err:
            raise HTTPException(status_code=500, detail=err)
        return {"stdout": out, "stderr": err}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
