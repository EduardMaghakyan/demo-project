from typing import Optional

from fastapi import Depends, FastAPI

from demo_setup.dependency_container import Application

app = FastAPI()


@app.get("/")
def read_root(app: Application = Depends()):
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.on_event("startup")
async def startup_event():
    Application()
