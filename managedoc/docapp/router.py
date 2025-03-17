from elrahapi.router.route_config import  AuthorizationConfig, RouteConfig
from elrahapi.router.router_default_routes_name import DefaultRoutesName
from managedoc.docapp.cruds import myapp_crud
from managedoc.settings.auth_configs import authentication
from typing import List
from elrahapi.router.router_provider import CustomRouterProvider

router_provider = CustomRouterProvider(
    prefix="/documents",
    tags=["document"],
    crud=myapp_crud,
    authentication= authentication,
    # roles=["MANAGER","ADMIN"]
)

# app_docapp = router_provider.get_public_router()
read_all_config=RouteConfig(
    route_name=DefaultRoutesName.READ_ALL,
    is_activated=True,
    is_protected=True,

)
authorizations:List[AuthorizationConfig]=[
    AuthorizationConfig(
        route_name = DefaultRoutesName.READ_ALL,
        privileges=["CAN_RETRIEVE_ALL_DOCUMENTS","CAN_RETRIEVE_ONE_DOCUMENT"]
    )
]

app_docapp = router_provider.initialize_router(
    init_data=[read_all_config],
    authorizations=authorizations
    )

# init_data: List[RouteConfig] = [
#     RouteConfig(route_name=DefaultRoutesName.CREATE, is_activated=True),
#     RouteConfig(route_name=DefaultRoutesName.READ_ONE, is_activated=True),
#     RouteConfig(route_name=DefaultRoutesName.READ_ALL, is_activated=True),
#     RouteConfig(route_name=DefaultRoutesName.UPDATE, is_activated=True, is_protected=True),
#     RouteConfig(route_name=DefaultRoutesName.DELETE, is_activated=True, is_protected=True),
# ]
# app_myapp = router_provider.initialize_router(init_data=init_data)
