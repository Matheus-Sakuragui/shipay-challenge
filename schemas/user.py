from marshmallow import Schema, fields
from config.schema import ma


class UserResponseSchema(ma.Schema):
    id = fields.Int()
    username = fields.Str()

    class Meta:
        fields = ("id", "name", "email", "role", "created_at", "updated_at")
        ordered = True


class UserRequestPostSchema(Schema):
    name = fields.Str(required=True, default='name', help='Invalid name')
    email = fields.Email(required=True, default='email', help='Invalid email')
    role_id = fields.Int(required=True, default='role_id', help='Invalid role id')
    password = fields.Str(required=False, help='Invalid password')



class UserRequestGetSchema(Schema):
    id = fields.Int(required=False, default='id', help='Invalid id')


user_schema = UserResponseSchema()
user_post_schema = UserRequestPostSchema()
