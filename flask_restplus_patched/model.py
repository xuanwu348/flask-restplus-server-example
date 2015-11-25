from apispec.ext.marshmallow.swagger import fields2jsonschema
from flask.ext import marshmallow
from werkzeug import cached_property

from flask_restplus.model import ApiModel as OriginalApiModel



class SchemaMixin(object):
   
    def __deepcopy__(self, memo):
        # XXX: Flask-RESTplus makes unnecessary data copying, while
        # marshmallow.Schema doesn't support deepcopyng.
        return self


class Schema(SchemaMixin, marshmallow.Schema):
    pass


if marshmallow.has_sqla:
    class ModelSchema(SchemaMixin, marshmallow.sqla.ModelSchema):
        pass


class DefaultHTTPErrorSchema(Schema):
    status = marshmallow.base_fields.Integer()
    message = marshmallow.base_fields.String()

    def __init__(self, http_code, **kwargs):
        super(DefaultHTTPErrorSchema, self).__init__(**kwargs)
        self.fields['status'].default = http_code


class ApiModel(OriginalApiModel):

    def __init__(self, model):
        # XXX: It is not a very elegant solution.
        super(ApiModel, self).__init__({'__schema__': model})

    @cached_property
    def __schema__(self):
        return fields2jsonschema(self['__schema__'].fields)