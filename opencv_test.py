import os

import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt, patches

# small test of cv2 template matching https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html

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
    return top_left, max_val


for image_file in ['screenshots/pg_sharp_teleport.png' ,'screenshots/open_gift.png', 'screenshots/main.png', 'screenshots/main_res_changed.png']:
    image = cv.imread(image_file)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    for template_file in os.listdir('templates/main'):
        template = cv.imread(f'templates/main/{template_file}')
        # All the 6 methods for comparison in a list
        (x, y), certaincy = process(methods[1], image, template)
        width, height = template.shape[:2]
        bottomright = (x + width, y + height)
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
        plt.gca().add_patch(rect)
        title = template_file.replace('.png', '').replace('_', ' ') + f' {certaincy * 100:.2f}%'
        plt.text(x + width + 10, y + height, title, color='red')
        print(title)
    print("-"*100)
    plt.savefig(image_file.replace('screenshots', 'tests'), dpi=300)
    plt.show()
