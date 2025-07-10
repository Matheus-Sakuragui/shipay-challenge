from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource
from marshmallow import fields

from models.roles import Role
from schemas.role import (RoleRequestGetSchema, RoleRequestPostSchema,
                                 RoleResponseSchema, role_schema)


@doc(description='Role API', tags=['Role'])
class RoleRegisterResource(MethodResource, Resource):
    @marshal_with(RoleResponseSchema, code='201')
    @use_kwargs(RoleRequestPostSchema, location='json')
    @doc(description='Register a new Role')
    def post(self, **kwargs):
        role = Role(
            description=kwargs['description']
        )
        role.save()
        return make_response(role, 201)
    
    @marshal_with(RoleRequestGetSchema, code='200')
    @use_kwargs(RoleRequestGetSchema, location='query')
    @doc(description='Get Role role by Role ID')
    def get(self, **kwargs):
        role_id = kwargs.get('id')
        role = Role.get_by_id(role_id)
        if not role:
            return make_response({"message": "Role not found"}, 404)
        return make_response(role_schema.dump({
            "id": role.id,
            "description": role.description,
            "users": [user.id for user in role.users]
        }), 200)