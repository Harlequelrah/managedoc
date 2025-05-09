from elrahapi.authentication.authentication_router_provider import AuthenticationRouterProvider
from managedoc.userapp.cruds import user_crud_models
from .secret import MAX_ATTEMPT_LOGIN
from .database import authentication

user_crud_models.sqlalchemy_model.MAX_ATTEMPT_LOGIN=MAX_ATTEMPT_LOGIN
authentication.authentication_models=user_crud_models
authentication_router_provider = AuthenticationRouterProvider(authentication=authentication)
authentication_router = authentication_router_provider.get_auth_router()







