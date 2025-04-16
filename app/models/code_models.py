from pydantic import BaseModel
from typing import List, Any

class TestCase(BaseModel):
    input: List[Any]
    expected_output: Any

class CodeExecutionRequest(BaseModel):
    code: str
    fn_name: str
    test_cases: List[TestCase]
