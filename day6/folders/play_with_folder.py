import os

PARENT_FOLDER = os.getcwd()
CURRENT_FOLDER = os.path.join(PARENT_FOLDER, "folders")
thamer_path = os.path.join(PARENT_FOLDER, "thamer")

print("The path of the parent folder: ", PARENT_FOLDER)
print("The path of the current folder: ", CURRENT_FOLDER)
# create new folder
os.mkdir(thamer_path)