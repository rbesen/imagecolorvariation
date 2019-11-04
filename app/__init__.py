# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from app.main.controller.image_controller import api as image_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Image APP API',
          version='1.0',
          description='API with flask restplus web service'
          )

api.add_namespace(image_ns, path='/process-image')
