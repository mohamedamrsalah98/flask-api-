from flask_restful import fields


category_serializer = {
    'id': fields.Integer,
    'name': fields.String,

}

post_serializer = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
    'category_id' : fields.Integer(),
    'category' : fields.Nested(category_serializer)


}


