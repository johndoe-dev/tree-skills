from flask_restplus import fields
from server.instance import server


book = server.api.model('Book', {
    'title': fields.String(required=True, min_length=1, max_length=200, description='Book title')
})
