import uvicorn

def run() -> None:
    uvicorn.run("fast_api_template.core.main:app", host="127.0.0.1", port=8000, reload=True)
