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
name_to_update = input("Enter contact name: ")
print("Note: if you do not want to update some details let it empty")
new_name = input("new name: ")
new_age = input("new age: ")
new_email = input("new email: ")
new_class = input("new class: ")
for contact in contacts:
    if contact["name"] == name_to_update:
        if len(new_name) > 0:
            contact["name"] = new_name
        if len(new_class) > 0:
            contact["class"] = new_class
        if len(new_age) > 0:
            contact["age"] = int(new_age)
        if len(new_email) > 0:
            contact["email"] = new_email
        path = os.path.join(project_path, name_to_update + ".json")
        with open(path, "w") as json_file:
            dump_contact = json.dumps(contact)
            json_file.write(dump_contact)
