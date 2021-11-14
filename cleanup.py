import os
import shutil

# script that cleans the original downloaded images taken from the https://conradsanderson.id.au/lfwcrop/ website

img_count = 8 # exact number of images you want from each person from the dataset

with open('lfw-names.txt') as f: # reads the names.txt file, which has the name and number of images of every person in the dataset
    lines = f.readlines()

names = [line.split()[0] for line in lines if int(line.split()[1]) >= img_count] # filters names based on the number of images they have


files = os.listdir('faces/') # name of the directory which has the person-specific subdirectories

wanted_names = ["Angelina_Jolie", "Antonio_Palocci", "Arnold_Schwarzenegger", "Bill_Clinton", "Bill_Gates", "Britney_Spears", "Catherine_Zeta-Jones", "Celine_Dion", "Charles_Moose", "Colin_Farrell", "David_Beckham", "Fernando_Gonzalez", "Fernando_Henrique_Cardoso", "Fidel_Castro", "George_Clooney", "George_W_Bush", "Gloria_Macapagal_Arroyo", "Halle_Berry", "Harrison_Ford", "Heizo_Takenaka", "Hillary_Clinton", "Hu_Jintao", "Hugh_Grant", "Hugo_Chavez", "Jackie_Chan", "James_Kelly", "Jelena_Dokic", "Jennifer_Aniston", "Jennifer_Garner", "Jennifer_Lopez", "Jesse_Jackson", "John_Paul_II", "Jose_Serra", "Julianne_Moore", "Julie_Gerberding", "Justin_Timberlake", "Kate_Hudson", "Keanu_Reeves", "Lance_Armstrong", "Laura_Bush", "Leonardo_DiCaprio", "Luiz_Inacio_Lula_da_Silva", "Maria_Shriver", "Meryl_Streep", "Michael_Jackson", "Michael_Schumacher", "Michelle_Kwan", "Naomi_Watts", "Nicole_Kidman", "Norah_Jones", "Pierce_Brosnan", "Queen_Elizabeth_II", "Ray_Romano", "Rubens_Barrichello", "Saddam_Hussein", "Salma_Hayek", "Serena_Williams", "Sheryl_Crow", "Sylvester_Stallone", "Tom_Cruise", "Tom_Hanks", "Vladimir_Putin"
]

for file in files:
    if "8" in file: # treats the file name string to match with the names on the txt file
        print(os.path.join('faces', file), os.path.join('objects', file))
        shutil.move(os.path.join('faces', file), os.path.join('objects', file))


# loop that counts the number of images of each person, and deletes the excess images if they have more than 8
# for name in names: 
#     count = 0
#     for file in files:
#         if file[:file.find('0')-1] == name:
#             count += 1
#             if count > img_count:
#                 print(file)
#                 os.remove(os.path.join('faces', file)) 

