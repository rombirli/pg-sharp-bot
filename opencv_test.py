import os

import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt, patches

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']


def process(meth, img, template):
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    return top_left


for image in ['main.png']:
    image = cv.imread(f'screenshots/{image}')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    for templatename in os.listdir('templates_for_main'):
        template = cv.imread(f'templates_for_main/{templatename}')
        # All the 6 methods for comparison in a list
        x, y = process(methods[1], image, template)
        width, height = template.shape[:2]
        bottomright = (x + width, y + height)
        rect = patches.Rectangle((x, y), width, height, linewidth=3, edgecolor='r', facecolor='none')
        plt.gca().add_patch(rect)
        plt.text(x + width + 10, y + height, templatename.replace('.png', '').replace('_', ' '), color='red')
    plt.savefig('patterns.png', dpi=300)
    plt.show()
