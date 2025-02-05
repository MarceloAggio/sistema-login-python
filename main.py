from fastapi import FastAPI
from routers import user, protected
from models import Base
from core.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(protected.router)
