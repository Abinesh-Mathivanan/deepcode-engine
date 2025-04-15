from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.code_execution import router as r

app = FastAPI()

# Add CORS middleware to allow requests from localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(r, prefix="/api/v1")
