import os
import json
working_directory_path = os.getcwd()
project_path = os.path.join(working_directory_path, "project")
list_of_all_files = os.listdir(project_path)
list_of_json_files = []
for file in list_of_all_files:
    if file.endswith(".json"):
        path = os.path.join(project_path, file)
        list_of_json_files.append(path)
contacts = []
for json_file in list_of_json_files:
    with open(json_file, "r") as json_file:
        json_content = json_file.read()
        content = json.loads(json_content)
        contacts.append(content)
name_to_search = input("Enter contact name: ")
for contact in contacts:
    if  contact["name"] == name_to_search:
        print(contact)