import sys
sys.path.append("./generator/")
from options.test_options import TestOptions
import urllib
import BytesIO
from PIL import Image


# this function should be called in written all
def deal_opt():
    opt = TestOptions().parse()
    opt.nThreads = 1  # test code only supports nThreads = 1
    opt.batchSize = 1  # test code only supports batchSize = 1
    opt.serial_batches = True  # no shuffle
    opt.no_flip = True  # no flip
    return opt


def urls2imgs(url):
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
