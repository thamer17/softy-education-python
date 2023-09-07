import os
import json
import pprint
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
search_input = input("What are you searching for: ")
result = {}
for contact in contacts:
    if search_input in contact["name"]:
        result = contact
print("The result of your search is: ", search_input)
if len(result) > 0:
    print(result)
else:
    print("Contact not found")