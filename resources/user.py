from flask import make_response
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource
from marshmallow import fields

from models.users import User
from schemas.user import (UserRequestGetSchema, UserRequestPostSchema,
                                 UserResponseSchema, user_schema)


@doc(description='User API', tags=['User'])
class UserRegisterResource(MethodResource, Resource):

    @marshal_with(UserResponseSchema, code='201')
    @use_kwargs(UserRequestPostSchema, location='json')
    @doc(description='Register a new user')
    def post(self, **kwargs):
        user = User(
            name=kwargs['name'],
            email=kwargs['email'],
            role_id=kwargs['role_id'],
            password=kwargs.get('password', None)
        )
        user.save()
        return make_response(user_schema.dump(user), 201)
    
    @marshal_with(UserRequestGetSchema, code='200')
    @use_kwargs(UserRequestGetSchema, location='query')
    @doc(description='Get user role by User ID')
    def get(self, **kwargs):
        user_id = kwargs.get('id')
        user = User.get_by_id(user_id)
        if not user:
            return make_response({"message": "User not found"}, 404)
        role = user.get_user_role()
        return make_response(user_schema.dump({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": role,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }), 200)
