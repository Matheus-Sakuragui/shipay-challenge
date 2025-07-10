from flask_restful import Api

from resources.user import UserRegisterResource, AddRoleToUserResource
from resources.role import RoleRegisterResource


def config_app_routes(app, docs):
    api = Api(app)
    __setting_route_doc(UserRegisterResource, '/user', api, docs)
    __setting_route_doc(AddRoleToUserResource, '/user/role', api, docs)
    __setting_route_doc(RoleRegisterResource, '/role', api, docs)

    return api


def __setting_route_doc(resource, route, api, docs):
    api.add_resource(resource, route)
    docs.register(resource)
