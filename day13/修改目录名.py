import os

os.chdir('../')

for resouce in os.listdir():
    if resouce.startswith('day') and len(resouce) == 4:
        os.rename(resouce, 'day0' + resouce[-1])
