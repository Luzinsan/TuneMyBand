# tunemyband/asgi/fastapi.py
from fastapi import FastAPI
from accounts.views import router as users_router
from equipment.views import router as equipment_router

app = FastAPI()


@app.get('/api/healthchecker')
def root():
    return {"message": 'Hello World!'}


app.include_router(users_router, tags=["auth"], prefix="")
app.include_router(equipment_router, tags=["equipment"], prefix="/equipment")

