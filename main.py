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
def analyze(code_input: CodeInput):
    try:
        tree = ast.parse(code_input.code)

        functions = [
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        ]

        explanation = f"Found {len(functions)} function(s) in your code."

        return {"functions": functions, "explanation": explanation}
    except SyntaxError as e:
        return {"error": f"Syntax Error: {str(e)}", "functions": [], "explanation": ""}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)