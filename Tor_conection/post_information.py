from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    gpu_model: str
    cpu_model: str
@app.post('/')
async def create_user(user_data: UserCreate):
    gpu = user_data.gpu_model
    print(gpu)
    return True

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
