from fastapi import FastAPI

app=FastAPI()

@app.get("/t.s")
def test():
    return {1:0}