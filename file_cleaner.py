import os, shutil, glob

path = os.chdir('/Users/Bryant/Documents') #can also change this line to take input for another directory

#can set a set a destination directory for the files to be moved to
#dest_directory =

#check the contents of directory selected
#files = os.listdir(path)

folder_list = ['txt', 'pdf', 'rtf', 'png', 'jpg', 'sh'] #folder names

#loop through folders names to create them
for folder in folder_list:
    if not os.path.exists(folder):
      os.makedirs(folder)
    else:
      print(f'Folder already exists, no folders created')        

#grab all file types in folder and save it to a variable 
txt_files = glob.glob('*.txt')
pdf_files = glob.glob('*.pdf')
rtf_files = glob.glob('*.rtf')
png_files = glob.glob('*.png')
jpg_files = glob.glob('*.jpg')
sh_files  = glob.glob('*.sh')



#loop through above variables to execute the move of the file
for file in txt_files:
    shutil.move(file, '/Users/Bryant/Documents/txt' )
for file in pdf_files:
    shutil.move(file, '/Users/Bryant/Documents/pdf')
for file in rtf_files:
    shutil.move(file, '/Users/Bryant/Documents/rtf')
for file in png_files:
    shutil.move(file,'/Users/Bryant/Documents/png')
for file in jpg_files:
    shutil.move(file, '/Users/Bryant/Documents/jpg')
for file in sh_files:
    shutil.move(file, '/Users/Bryant/Documents/sh')
