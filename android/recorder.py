import os

filename = input('enter a name for this record : ')
print('Starting recording. press ^C to escape')

os.system(f'adb shell getevent -t > ../records/{filename}')

