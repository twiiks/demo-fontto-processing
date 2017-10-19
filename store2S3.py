from io import BytesIO
import boto3
import time
from time import strftime
from time import gmtime
from flask import Flask, request
import json

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)

"""
1. s3로 올리는 것
2. flask request, response
"""
def store2S3(uni, image_PIL, count, env):
    # PIL to base64 buffer 
    buffer = BytesIO()
    image_PIL.save(buffer, format='JPEG')
    image_base64 = base64.b64encode(buffer.getvalue())
    
    # buffer to s3
    time_gm = time.gmtime(time.time())
    time_stemp = strftime("%y-%m-%d-%H-%M-%S-000", time_gm) #returns 17-10-19-15-18-000
    s3 = boto3.resource('s3')
    s3.Bucket('fontto'). \
            put_object(Key='%s/handwrites/fontto@twiiks.co/%s/%s_%s' %(env, count, time_stemp, "'가'"), Body=base64.b64decode(image_base64), ContentType='image/jpeg', ACL='public_read')


def backgroundProcessing(request):
    body = request.json
    input_urls = body['urls']
    count = body['count']
    env = body['env']
    url_class = fontto2pix2pix(input_urls, count, env)

    return url_class


@app.route('/fontto/processing', methods=['POST'])
def processing_fontto():
    return json.dumps(backgroundProcessing(request))
    
    
@app.route('/connection-test')
def test_root():
    return 'OK'


if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5959)
    IOLoop.instance().start()
    # app.run(port=5959, debug=True)
   
