from fastapi import FastAPI

from app.core import Base
from app.core.database import engine
from app.endpoints import router as endpoints_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(endpoints_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create all tables in the database
# @app.on_event("startup")
# async def startup():
#     Base.metadata.create_all(bind=engine)