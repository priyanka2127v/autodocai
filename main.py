from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ast

app = FastAPI()

# 🔥 VERY IMPORTANT (for frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.get("/")
def home():
    return {"message": "AutoDoc AI Running 🚀"}

@app.post("/analyze")
def analyze(code_input: CodeInput):
    tree = ast.parse(code_input.code)

    functions = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    ]

    return {"functions": functions}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)