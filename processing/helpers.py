from PIL import Image
import numpy as np


def load_picture(filename: str):
    pic = Image.open(filename)
    pix = np.array(pic, dtype=int)
    return pix
