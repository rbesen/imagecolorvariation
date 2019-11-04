from flask import request, session
from flask_restplus import Resource
from flask_cors import cross_origin
from flask_restplus import Namespace, fields, marshal
import json
from PIL import Image

api = Namespace('process-image')

@api.route('/')
@api.response(200, 'Ok.')
class ShopList(Resource):
  @api.doc('Receive image and coordinates')
  def post(self):
    data = request.json
    im = Image.open(data.get('image_url'))
    coefficient = None#call service
    return coefficient
