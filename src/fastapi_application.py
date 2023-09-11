import uvicorn

from fastapi_asgi import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5002)
