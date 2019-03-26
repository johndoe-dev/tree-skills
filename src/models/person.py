from flask_restplus import fields
from server.instance import server


person = server.api.model('Person', {
    'name': fields.String(required=True, min_length=1, max_length=200, description='Person name'),

})


