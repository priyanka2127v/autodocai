from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ast

app = FastAPI()

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
def analyze(input: CodeInput):
    code = input.code

    # 🔹 Extract functions (Python)
    functions = []
    try:
        tree = ast.parse(code)
        functions = [
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        ]
    except:
        return {"error": "Invalid Python code"}

    # 🔹 Simple explanation logic (NO API needed 🔥)
    explanation = "This code contains the following functions:\n"

    for func in functions:
        explanation += f"- {func}(): This function performs a specific operation.\n"

    if not functions:
        explanation = "No functions found in the given code."

    return {
        "functions": functions,
        "explanation": explanation
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)