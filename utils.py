import sys
sys.path.append("./generator/")
from options.test_options import TestOptions
import urllib
from io import BytesIO
from PIL import Image
import base64
import time
from time import strftime
from time import gmtime
import boto3


# this function should be called in written all
def deal_opt():
    opt = TestOptions().parse()
    opt.nThreads = 1  # test code only supports nThreads = 1
    opt.batchSize = 1  # test code only supports batchSize = 1
    opt.serial_batches = True  # no shuffle
    opt.no_flip = True  # no flip
    return opt


def url2img(url):
    """
    - fontto_pix2pix에서 사용할 수 있도록 url을 통해 이미지를 로드하고 PIL Image로 변환하여 반환
    - 입력 : url
    - 반환 : image
    """
    #url -> bytes
    url = urllib.request.urlopen(url).read()
    bytesFromS3 = BytesIO(url)
    #bytes -> image
    imgFromS3 = Image.open(bytesFromS3)
    #    imgFromS3.show()

    return imgFromS3


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
