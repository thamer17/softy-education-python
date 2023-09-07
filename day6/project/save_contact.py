import json
import os
contact = {
    "name": input('name: '), 
    "age": int(input("age: ")), 
    "email": input("email: "), 
    "class": input("class: ")
}
working_directory_path = os.getcwd()
project_path = os.path.join(working_directory_path, "project")
json_file_path = os.path.join(project_path, contact["name"] + ".json")
with open(json_file_path, "w") as json_file :
    dump_content = json.dumps(contact)
    json_file.write(dump_content)
