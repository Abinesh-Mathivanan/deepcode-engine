from fastapi import FastAPI
from api.v1.code_execution import router as r

app = FastAPI()
app.include_router(r, prefix="/api/v1")
