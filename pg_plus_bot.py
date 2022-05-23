import sys

import matplotlib.pyplot as plt

from android.controller import *
from processing.helpers import load_picture


def is_pgplus_enabled():
    img = load_picture('screen.png')
    x, y, width, height = map(int, open('templates/pgplus_enabled.txt'))
    subim = img[y:y + height, x:x + width, :-1]
    plt.imshow(subim)
    plt.show()
    return (subim == load_picture('templates/pgplus_enabled.png')).all()


def is_pgsharp_icon_here():
    img = load_picture('screen.png')
    x, y, width, height = map(int, open('templates/pgsharp.txt'))
    subim = img[y:y + height, x:x + width, :-1]
    plt.imshow(subim)
    plt.show()
    return (subim == load_picture('templates/pgsharp.png')).all()


saragosse_1, saragosse_2 = '41.660830,-0.892046', '41.662138,-0.894597'


def walk_to(destination):
    print(f'walking to {destination}')
    tap(86, 303)
    sleep(.5)
    tap(98, 214)
    sleep(.5)
    tap(400, 208)
    write(destination)
    tap(993, 2185)
    sleep(.5)
    tap(653, 1054)
    sleep(.5)
    tap(975, 220)
    for i in range(70, 0, -1):
        sys.stdout.write(f'\rwaiting... {i}')
        sleep(1)
    sys.stdout.write(f'\r')


while True:
    screenshot('screen.png')
    if not is_pgplus_enabled():
        tap(991, 525)
        sleep(10)
    if not is_pgplus_enabled():
        print('couldnot enable pgplus')
        continue
    print('pgplus enabled !')
    if is_pgsharp_icon_here():
        walk_to(saragosse_1)
    if is_pgsharp_icon_here():
        walk_to(saragosse_2)
