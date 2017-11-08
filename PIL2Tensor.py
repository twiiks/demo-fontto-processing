import torch.utils.data as data
from PIL import Image
import torchvision.transforms as transforms


def get_transform():
    transform_list = []
    transform_list += [
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ]
    return transforms.Compose(transform_list)


def to_tensor(input_image):
    transform = get_transform()
    output_tensor = transform(input_image)
    return output_tensor
