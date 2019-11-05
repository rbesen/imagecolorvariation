# imagecolorvariation
Compute the coefficient of variation of a square inside an image

Pre-requisites:
Python 3
Pip

To run the project: 

Clone from repository

Import dependencies 
  - pip install -r requirements.txt

Execute application server:
  - python3 manage.py run

The serve will expose the api in port 5000, the only endpoint available is:
  - POST - localhost:5000/process-image/
  - The endpoint expect a json object with the following params
  {"imageUrl": "IMAGE_URL_STRING",
    "regionOfInterest": {
      "top": float,
      "left": float,
      "right": float,
      "bottom": float
    }
  }

  Ex.: 
  {"imageUrl": "https://s3.envato.com/files/223920975/Low%20Poly%20Colorful%20Background%20Preview.jpg",
    "regionOfInterest": {
    "top": 0.25,
    "left": 0.1,
    "right": 0.25,
    "bottom": 0.5
    }
  }

  The answer for this request will be:
  {
    "cv_r": 0.707593389320159,
    "cv_g": 0.6696987224983962,
    "cv_b": 0.4073231239656784
  }

  If one of the parameters are missing you will receive a 422 response code.

Limitations:

For now is only working with JPG, because PNG and GIF have a differente color scale.
I didn't create tests, should test service methods and create an integration test.
The parameters validation should be done by restplus and documented with swagger. The endpoint is documented, params not.