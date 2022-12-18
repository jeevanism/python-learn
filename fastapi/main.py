
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def welcome():
    return {
        "message":"Welcome to fast API"
    }

   
@app.get("/username/{userName}")
async def readUsername(userName: str):
    return {
        "message": "Welcome "+ userName.capitalize()
    }
    
userDetails = [
    {
        "userName":"Jeevan"
    }
] 
@app.get("/userdetails/")
async def reaUserDetails(name: str, age: int):
    userDetails = {
        "name":name,
        "age":age        
    }
    return userDetails