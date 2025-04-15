# backend/api/v1/code_execution.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class CodeInput(BaseModel):
    code: str

@router.post("/execute_code")
async def run_code(data: CodeInput):
    # Replace this with actual code execution logic
    return {"result": "success"}
