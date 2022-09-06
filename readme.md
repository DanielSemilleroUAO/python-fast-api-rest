# Dos maneras de ejecutar FastAPI

Ejecutar desde la shell
```
uvicorn main:app
```

Agregar las líneas de código
```
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
```
Luego ejecutar main.py