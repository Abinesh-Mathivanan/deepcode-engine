from pydantic import BaseModel
from typing import List

class TestCase(BaseModel):
    input: str
    expected_output: str

class CodeExecutionRequest(BaseModel):
    code: str
    fn_name: str
    test_cases: List[TestCase]
