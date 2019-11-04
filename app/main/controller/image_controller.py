from flask import request, session
from flask_restplus import Resource
from flask_cors import cross_origin
from flask_restplus import Namespace, fields, marshal
import json
from PIL import Image
import urllib.request

api = Namespace('process-image')

@api.route('/')
@api.response(200, 'Ok.')
class ShopList(Resource):
  def post(self):
    print(request)
    data = request.json
    im = Image.open(urllib.request.urlopen(data.get('imageUrl')))
    print(im.size)
    #coefficient = None#call service
    #return coefficient
