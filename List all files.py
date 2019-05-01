#An awesome program to write all the filenames of the given path to a file

import glob

path = 'C:\\'            #Add path here

filename ='my_database.txt'
files = [f for f in glob.glob(path + "**/**/*.*", recursive=True)]

with open(filename, 'w', encoding="utf-8") as fout:
    for f in files:
        print(f)
        fout.write( f+'\n' )
