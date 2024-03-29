import uvicorn


from fastapi import FastAPI
from route_produtos import router as produto_router
from route_usuario import router as usuario_router

app = FastAPI()

@app.get('/')
def link():
    return ("vá para localhost:8003/docs")


@app.get('/health-check')
def health_check():
    return True

app.include_router(produto_router)

app.include_router(usuario_router)

if __name__ == "__main__":
    import uvicorn
#                  #nomearquivo#nomeAppMain   
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)