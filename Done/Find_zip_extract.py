import zipfile
import os
import re
zip_list = []

def find_zip_files():

#Looking fot zip_files, storing them in the zip_list.
#Returning list of zip_files, if no zip_files found, return notification.
#Ziplife module // ziplife.is_ziplife(filename) would be the go. 
    
    folder = os.listdir()
    print("\n\n")
    print("Found:")
    print("\n")
    for file in folder:
        if (re.findall(r'\.zip$',file)) == [".zip"]:
            print(f"\t {file}")
            zip_list.append(file)
                   
    if zip_list:
        return zip_list
    else:
        return "No zipped files found."
        
        
def open_zip_files():

# Extracting zip_files found from find_zip_files().
# Creating a new folder for extracted files. Getting still errors with * or others.
# Still work to do. 

    while True: 
        try:
            folder_name = str(input(f"Please provide a folder name for zip_files at {os.getcwd()} directory."))
        except:
            print("ERROR! Folder not created. Try one more time.") 
        else:
            print(f"\nFolder {folder_name} created successfully.")
            break
            
    print("Unpacking files:")
    for zip_file in zip_list:
        myZip = zipfile.ZipFile(zip_file)
        print(f'\t {myZip}')
        myZip.extractall(folder_name)
        
        
def switch_zip_files():
    
#After having list of stored zip_files - ask user if to extract them to a file.

    while True:
        if input("\nDo you want to extract all the files? y/n").lower()[0] == "y":
            return True
        else:
            return False
            
#--------------------------------
#Putting funcs together into one
#--------------------------------

print("Looking for zipped files at directory:")
print(f'{os.getcwd()}')

if find_zip_files():
    if switch_zip_files():
        open_zip_files()
    else:
        print("Extracting denied. Closing script.")
else:
    print("Closing script.")
zip_list = []

