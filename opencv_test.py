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
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right


for image in ['main.png']:
    image = cv.imread(f'screenshots/{image}', 0)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    for templatename in os.listdir('templates_for_main'):
        template = cv.imread(f'templates_for_main/{templatename}', 0)
        w, h = template.shape[::-1]
        # All the 6 methods for comparison in a list
        topleft, bottomright = process(methods[1], image, template)
        (x0, y0), (x1, y1) = topleft, bottomright
        center = (x0 + x1) / 2, (y0 + y1) / 2
        rect = patches.Rectangle(bottomright, x0 - x1, y0 - y1, linewidth=3, edgecolor='r', facecolor='none')
        plt.gca().add_patch(rect)
        plt.text(x1 + 10, y1, templatename.replace('.png', '').replace('_', ' '), color='red')
    plt.savefig('patterns.png', dpi=300)
    plt.show()
