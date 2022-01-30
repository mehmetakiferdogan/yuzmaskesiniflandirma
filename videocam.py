import imutils
import cv2
import predict

import base64
import numpy as np


def processFrame(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img=predict.predictFrame(img)
    retval, buffer = cv2.imencode('.jpg', img)
    #   jpg_as_text =buffer.tobytes()  
    jpg_as_text = base64.b64encode(buffer)

    yield (jpg_as_text)#sadece b ytes  


