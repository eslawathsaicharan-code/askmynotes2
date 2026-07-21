from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"message":"hello fastapi"}

@app.get("/greet")
def greet_user(name:str):
    return {"message": "hello, "+name +" !"}