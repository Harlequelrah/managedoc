
from elrahapi.router.router_default_routes_name import DefaultRoutesName
from elrahapi.router.router_provider import CustomRouterProvider
from .cruds import user_crud,user_privilege_crud,role_crud,privilege_crud,role_privilege_crud
from managedoc.settings.auth_configs import authentication


user_router_provider = CustomRouterProvider(
    prefix="/users",
    tags=["users"],
    crud=user_crud,
    authentication=authentication,
)

user_privilege_router_provider=CustomRouterProvider(
    prefix='/users/privileges',
    tags=["users_privileges"],
    crud=user_privilege_crud,
    authentication=authentication,
)

role_router_provider = CustomRouterProvider(
    prefix="/roles",
    tags=["roles"],
    crud=role_crud,
    authentication=authentication,
)

privilege_router_provider = CustomRouterProvider(
    prefix="/privileges",
    tags=["privileges"],
    crud=privilege_crud,
    authentication=authentication,
)



role_privilege_router_provider=CustomRouterProvider(
    prefix='/roles/privileges',
    tags=["roles_privileges"],
    crud=role_privilege_crud,
    authentication=authentication,
)

user_router = user_router_provider.get_custom_public_router(
    public_routes_name=[
        DefaultRoutesName.BULK_CREATE,
        DefaultRoutesName.READ_ALL,
        DefaultRoutesName.CREATE
    ]
)

user_privilege_router=user_privilege_router_provider.get_protected_router()

role_router=role_router_provider.get_protected_router()

privilege_router=privilege_router_provider.get_protected_router()

role_privilege_router=role_privilege_router_provider.get_protected_router()
