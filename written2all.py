#one2class
import sys
sys.path.append("./generator/")

import os
from PIL import Image
from generator import generator
from PIL2Tensor import to_tensor

#written2all
from utils import deal_opt


def one2class(unicode_input, image_input, opt):
    path_class = "./pths/%s/" % (unicode_input)
    if not os.path.isdir(path_class):
        return {}

    images_output = {}

    # change image type to tensor float
    image_input_tensor = to_tensor(image_input)
    image_input_tensor = image_input_tensor.unsqueeze(0)

    # if pth exist, generate another character using pth
    dirs = os.listdir(path_class)
    for dir in dirs:
        if dir.split('_')[0] == unicode_input:
            files = os.listdir("%s/%s/" % (path_class, dir))
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.pth':
                    unicode_output = dir.split('_')[1].split('.')[-1]
                    # log
                    print("now dealing with :", unicode_output)
                    path_pth = os.path.abspath("%s/%s/%s" % (path_class, dir,
                                                             filename))
                    image_gen = generator(image_input_tensor, opt, path_pth)
                    images_output[unicode_output] = image_gen
                    break

    return images_output


def written2all(unicode_image):
    opt = deal_opt()
    image_output = {}

    for unicode_input, image_input in unicode_image.items():
        # print log
        print('written2all : now dealing unicode [%s]' % unicode_input)
        img_gen = one2class(unicode_input, image_input, opt)
        image_output.update(img_gen)
    return image_output