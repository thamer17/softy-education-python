import json
import os

working_directory_path = os.getcwd()
print(working_directory_path)
path_to_os_folder = os.path.join(working_directory_path, "os")
print("path: ", path_to_os_folder)
# file exists or not
os_folder_exists = os.path.exists(path_to_os_folder)
print(os_folder_exists)
if(not os_folder_exists):
    os.mkdir(path_to_os_folder)
path_to_data_json_file = os.path.join(path_to_os_folder, "data.json")
# create a json
data = {
    "language": "Python", 
    "score": 10
}
with open(path_to_data_json_file, "w") as json_file:
    #conversion
    json_content = json.dumps(data)
    
    json_file.write(json_content)
with open(path_to_data_json_file, "r") as json_file:

    json_content = json_file.read()
    
    content = json.loads(json_content)
    print(content)         