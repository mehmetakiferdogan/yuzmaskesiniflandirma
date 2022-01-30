# -*- coding: utf-8 -*-
from flask import Flask, url_for, redirect
from flask import render_template,Response
from flask import request
import videocam

app = Flask(__name__,static_folder="web/static",template_folder='web/templates')

@app.route('/video_feed', methods=['GET','POST'])
def video_feed():
    postData = request.get_json()
    return Response(videocam.processFrame(postData["frame"]), mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/')
def index():
    return render_template('index.html')

#CMDDEN CALISTIRIRKREN BUNU UNCOMMENTLE:
#if __name__ == "__main__":
#  app.run()