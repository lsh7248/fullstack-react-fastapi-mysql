"""
Owner: LSH
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    :return: Hello World
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    :param
    - **name** :My Name

    :return: Hello Name
    """
    return {"message": f"Hello {name}"}
