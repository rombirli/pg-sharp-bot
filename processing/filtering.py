import numpy as np



def filter_color(image: np.array, color: (int, int, int), max_diff: (int, int, int) = (30, 30, 30)):
    diffr, diffg, diffb = max_diff
    collr, collg, collb = color
    return ((collr - diffr) <= image[:, :, 0]) & (image[:, :, 0] <= (collr + diffr)) & \
           ((collg - diffg) <= image[:, :, 1]) & (image[:, :, 1] <= (collg + diffg)) & \
           ((collb - diffb) <= image[:, :, 2]) & (image[:, :, 2] <= (collb + diffb))


def apply_filter(filtered, image):
    image_new = image.copy()
    image_new[:, :, 0] = image_new[:, :, 0] * filtered
    image_new[:, :, 1] = image_new[:, :, 1] * filtered
    image_new[:, :, 2] = image_new[:, :, 2] * filtered
    return image_new


class Filters:
    @classmethod
    def pgsharp(cls, image: np.array):
        return filter_color(image, (255, 170, 0)) | \
               filter_color(image, (255, 208, 11))


    @classmethod
    def pokestops(cls, image: np.array):
        return filter_color(image, (60, 240, 255)) | \
               filter_color(image, (30, 117, 230))

    @classmethod
    def sea(cls, image: np.array):
        return filter_color(image, (38, 78, 133), (10, 10, 10)) | \
               filter_color(image, (67, 89, 125), (10, 10, 10))

    @classmethod
    def road_grey(cls, image: np.array):
        return filter_color(image, (79, 147, 136))

    @classmethod
    def road_yellow(cls, image: np.array):
        return filter_color(image, (255, 255, 148))

    @classmethod
    def land(cls, image: np.array):
        return filter_color(image, (11, 165, 135), (70, 70, 40))
