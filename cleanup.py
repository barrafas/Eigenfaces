import os
import shutil

with open('lfw-names.txt') as f:
    lines = f.readlines()

names = [line.split()[0] for line in lines if line.split()[1] == "5"]

dirs = os.listdir('lfw-deepfunneled/')
destination = 'images'
for dir in dirs:
    if dir not in names:
        for file in os.listdir(os.path.join('lfw-deepfunneled', dir)):
            os.remove(os.path.join('lfw-deepfunneled', dir, file))
    else:
        for file in os.listdir(os.path.join('lfw-deepfunneled', dir)):
            shutil.move(os.path.join('lfw-deepfunneled', dir, file), os.path.join(destination, file))



