from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = "mysql+pymsql://root:password@localhost/bookexchange"
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}

@app.get("/profile")
def profile():
    return