import os

# script that cleans the original downloaded images taken from the https://conradsanderson.id.au/lfwcrop/ website

img_count = 8 # exact number of images you want from each person from the dataset

with open('lfw-names.txt') as f: # reads the names.txt file, which has the name and number of images of every person in the dataset
    lines = f.readlines()

names = [line.split()[0] for line in lines if int(line.split()[1]) >= img_count] # filters names based on the number of images they have


files = os.listdir('faces/') # name of the directory which has the person-specific subdirectories

for file in files:
    if file[:file.find('0')-1] not in names: # treats the file name string to match with the names on the txt file
        print(file)
        os.remove(os.path.join('faces', file)) # removes files from names that don't have 8 or more images


# loop that counts the number of images of each person, and deletes the excess images if they have more than 8
for name in names: 
    count = 0
    for file in files:
        if file[:file.find('0')-1] == name:
            count += 1
            if count > img_count:
                print(file)
                os.remove(os.path.join('faces', file)) 
        
print(names)
