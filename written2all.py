from PIL import Image
from utils import deal_opt
from one2class import one2class

def written2all(unicode_image):
    opt = deal_opt()
    image_output = {}

    for unicode_input, image_input in unicode_image.items():
        # print log
        print('written2all : now dealing unicode [%s]' % unicode_input)
        img_gen = one2class(unicode_input, image_input, opt)
        image_output.update(img_gen)
    return image_output
