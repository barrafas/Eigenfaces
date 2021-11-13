import os

with open('lfw-names.txt') as f:
    lines = f.readlines()

names = [line.split()[0] for line in lines if line.split()[1] == "5"]

dirs = os.listdir('lfw-deepfunneled/')
for dir in dirs:
    if dir not in names:
        for file in os.listdir(os.path.join('lfw-deepfunneled', dir)):
            os.remove(os.path.join('lfw-deepfunneled', dir, file))
