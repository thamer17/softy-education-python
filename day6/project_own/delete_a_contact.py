import os
working_directory_path = os.getcwd()
project_path = os.path.join(working_directory_path, "project")
name_to_delete = input("Enter contact name: ")
file_to_delete = os.path.join(project_path, name_to_delete + ".json")
os.remove(file_to_delete)