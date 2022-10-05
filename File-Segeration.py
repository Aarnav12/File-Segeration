import os
import shutil

source = 'C:/Users/sapsl/Downloads/Whitehat jr Python/C102/Source File'
destination = 'C:/Users/sapsl/Downloads/Whitehat jr Python/C102/Moved Image'

list_of_files = os.listdir(source)

#print(list_of_files)

for file in list_of_files:
    name,ext = os.path.splitext(file)
    #print(name)
    #print(ext)
    if ext == '':
        continue
    elif ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + file
        #path2 =destination + '/' + file
        print("moving" + file + '....')
        shutil.move(path1,destination)