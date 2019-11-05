import requests
import os
import threading
from PIL import Image
import statistics

def calculate_color_cv_of_image_region(image, region):
  #exclude right and bottom pixel
  box = image.crop((region.get('left'), region.get('top'), region.get('right')-1, region.get('bottom')-1))
  red = list(box.getdata(band=0))
  green = list(box.getdata(band=1))
  blue = list(box.getdata(band=2))
  cv_red = statistics.stdev(red)/statistics.mean(red)
  cv_blue = statistics.stdev(red)/statistics.mean(blue)
  cv_green = statistics.stdev(red)/statistics.mean(green)
  
  return (cv_red, cv_green, cv_blue)

def calculate_region(image, presets):
  (width, height) = image.size
  top = height * float(presets.get('top'))
  left = width * float(presets.get('left'))
  bottom = height * float(presets.get('bottom'))
  right = width * float(presets.get('right'))
  region = {'top': top, 'left': left, 'bottom': bottom,'right': right}
  return region

