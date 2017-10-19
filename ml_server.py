from fontto_pix2pix import fontto_pix2pix 
import json
from flask import Flask, request

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)

def backgroundProcessing(request):
    body = request.json
    input_urls = body['urls']
    count = body['count']
    env = body['env']
    url_class = fontto_pix2pix(input_urls, count, env)

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
