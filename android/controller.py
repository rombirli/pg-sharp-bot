from time import sleep
import numpy as np
from ppadb.client import Client
from PIL import Image

from .events import Event

adb = Client(host='127.0.0.1', port=5037)
device = adb.devices()[0]


def screenshot(filename='screen.png') -> np.array:
    image = device.screencap()
    with open(filename, 'wb') as f:
        f.write(image)
    pic = Image.open(filename)
    pix = np.array(pic, dtype=int)
    return pix


def tap(x: int, y: int):
    device.shell(f'input tap {x} {y}')


def write(s: str):
    device.shell(f'input text "{s}"')


def swipe(from_x: int, from_y: int, to_x: int, to_y: int, duration: float):
    device.shell(f'input swipe {from_x} {from_y} {to_x} {to_y} {duration}')


def send_event(event: Event):
    device.shell(f'input keyevent {event.keycode}')


def play_record(filename: str):
    lasttime = None
    for line in open(f'records/{filename}'):
        if line.startswith('['):
            time, line = line.split(']')
            time = float(time.replace('[', '').strip())
            if lasttime is not None:
                sleep(time - lasttime)
            lasttime = time
            event, hexcode = map(str.strip, line.split(':'))
            print(time, event, hexcode)
            device.shell(f'sendevent {event} {hexcode}')
