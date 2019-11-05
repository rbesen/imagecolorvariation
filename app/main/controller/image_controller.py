from flask import request
from flask_restplus import Resource
from flask_restplus import Namespace
from app.main.service.process_colors_service import calculate_region, calculate_color_cv_of_image_region
import json
from PIL import Image
import urllib.request

api = Namespace('process-image')

@api.route('/')
@api.response(200, 'Ok.')
class ShopList(Resource):
  def post(self):
    data = request.json
    if(data.get('imageUrl') == None or data.get('regionOfInterest') == None):
      api.abort(422)
    image = Image.open(urllib.request.urlopen(data.get('imageUrl')))
    region = calculate_region(image, data.get('regionOfInterest'))
    cv_red, cv_green, cv_blue = calculate_color_cv_of_image_region(image, region)
    return {'cv_r': cv_red, 'cv_g': cv_green, 'cv_b': cv_blue}
    
