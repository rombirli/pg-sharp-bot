import os

import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt, patches

# small test of cv2 template matching https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']


def process(meth, img, template) -> ((int, int), float):
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img, template, method)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    return tuple(top_left), max_val


template_files = [f'templates/main/{f}' for f in os.listdir('templates/main')] + \
                 [f'templates/pg_sharp_menu/{f}' for f in os.listdir('templates/pg_sharp_menu')] + \
                 [f'templates/{f}' for f in os.listdir('templates') if '.png' in f]
for image_file in os.listdir('screenshots'):
    image = cv.imread(f'screenshots/{image_file}')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    print(image_file)
    for template_file in template_files:
        template = cv.imread(template_file)
        # All the 6 methods for comparison in a list
        (x, y), score = process(methods[1], image, template)
        if score < 0.90: continue
        height, width = template.shape[:2]
        bottomright = (x + width, y + height)
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
        plt.gca().add_patch(rect)
        title = template_file.split('/')[-1].replace('.png', '').replace('_', ' ') + f' {score * 100:.2f}%'
        plt.text(x + width + 10, y + height, title, color='red')
        print(title)
    print("-" * 100)
    plt.savefig(f'tests/{image_file}', dpi=300)
    plt.show()
