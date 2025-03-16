from fastapi import FastAPI
from managedoc.settings.database import engine, authentication
from managedoc.settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from managedoc.docapp.router import app_docapp

app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(app_docapp)
app.add_middleware(
    ErrorHandlingMiddleware,
)

