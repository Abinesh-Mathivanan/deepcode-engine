from fastapi import APIRouter
from models.code_models import CodeExecutionRequest
from ..services.executor import run_code

router = APIRouter()

@router.post("/execute")
def execute_code(payload: CodeExecutionRequest):
    return run_code(payload.code, payload.fn_name, payload.test_cases)
