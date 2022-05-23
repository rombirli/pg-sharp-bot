from android.controller import screenshot

while True:
    filename = input('enter filename : ')
    if filename == 'q': quit()
    screenshot(f'screenshots/{filename}.png')
