import os

#create a variable with the script name
filename = os.path.basename(__file__)

#list the directories in the current folder
dir_list = os.listdir()
print(dir_list)

#loop to delete the files in the folder | if the file == the script name, continue
for file in dir_list:
    if file == filename:
        continue
    else:
        #print the file that is being removed
        print(F"Removing file: {file}")
        os.remove(file)

#print a message after the successful run
print("All files were removed besides the python file")

