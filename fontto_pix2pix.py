from utils import deal_opt, url2img, store2S3
from written2all import written2all


def fontto_pix2pix(input_unicode_url, count, env):
    '''
    - input
     - unicode_urls = {unicode : url}
     - count = int
     - env = string
    - output
     - output_unicode_url = {unicode : url}
    '''

    # change urls to images
    input_unicode_image = {}
    for input_unicode, input_url in input_unicode_url.items():
        input_image = url2img(input_url)
        input_unicode_image[input_unicode] = input_image

    # generate images
    output_unicode_image = written2all(input_unicode_image)

    # store generated images to S3
    output_unicode_url = {}
    for output_unicode, output_image in output_unicode_image.items():
        output_url = store2S3(output_unicode, output_image, count, env)
        output_unicode_url[output_unicode] = output_url

    return output_unicode_url 
