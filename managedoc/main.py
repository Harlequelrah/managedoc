from fastapi import FastAPI
from managedoc.settings.database import engine, authentication
from managedoc.settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from managedoc.docapp.router import app_docapp
from managedoc.userapp.routers import user_router,user_privilege_router,role_router,role_privilege_router,privilege_router
from managedoc.settings.auth_configs import authentication_router
app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(app_docapp)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(privilege_router)
app.include_router(role_privilege_router)
app.include_router(user_privilege_router)
app.include_router(authentication_router)
app.add_middleware(
    ErrorHandlingMiddleware,
)

