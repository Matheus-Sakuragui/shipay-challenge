from marshmallow import Schema, fields
from config.schema import ma


class RoleResponseSchema(ma.Schema):
    id = fields.Int()
    description = fields.Str()
    users = fields.List(fields.Int(), attribute='users', dump_only=True)

    class Meta:
        fields = ("id", "description", "users")
        ordered = True


class RoleRequestPostSchema(Schema):
    description = fields.Str(required=True, default='description', help='Invalid description')



class RoleRequestGetSchema(Schema):
    id = fields.Int(required=False, default='id', help='Invalid id')


role_schema = RoleResponseSchema()
role_post_schema = RoleRequestPostSchema()
