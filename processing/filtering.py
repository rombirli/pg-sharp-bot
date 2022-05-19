import numpy as np


def all(image: np.array):
    return (0x00 <= image[:, :, 0]) & (image[:, :, 0] <= 0xff) & \
           (0x00 <= image[:, :, 1]) & (image[:, :, 1] <= 0xff) & \
           (0x00 <= image[:, :, 2]) & (image[:, :, 2] <= 0xff)


def pokestops(image: np.array):
    return (20 <= image[:, :, 0]) & (image[:, :, 0] <= 40) & \
           (100 <= image[:, :, 1]) & (image[:, :, 1] <= 215) & \
           (220 <= image[:, :, 2]) & (image[:, :, 2] <= 255)

def pgsharp(image: np.array):
    return (0xf0 <= image[:, :, 0]) & (image[:, :, 0] <= 0xff) & \
           (0xa0 <= image[:, :, 1]) & (image[:, :, 1] <= 0xcf) & \
           (0x00 <= image[:, :, 2]) & (image[:, :, 2] <= 0x10)


def apply_filter(filter, image):
    filtered = filter(image)
    image_new = image.copy()
    image_new[:, :, 0] = image_new[:, :, 0] * filtered
    image_new[:, :, 1] = image_new[:, :, 1] * filtered
    image_new[:, :, 2] = image_new[:, :, 2] * filtered
    return image_new
