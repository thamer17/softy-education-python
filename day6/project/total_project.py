import json
import os
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
def save_contact():
    contact = {
    "name": input('name: '), 
    "age": int(input("age: ")), 
    "email": input("email: "), 
    "class": input("class: ")
    }
    json_file_path = os.path.join(project_path, contact["name"] + ".json")
    with open(json_file_path, "w") as json_file :
        dump_content = json.dumps(contact)
        json_file.write(dump_content)

def list_of_contacts():
    pprint.pprint(contacts)

def search():
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

def update():
    search_input = input("Enter the name of contact you want to update : ")
    result = {}
    for contact in contacts:
        if search_input in contact["name"]:
            result = contact
    if len(result) > 0:
        result["age"] = 18
        path = os.path.join(project_path, search_input + ".json")
        with open(path, "w") as json_file:
            dump_content = json.dumps(result)
            json_file.write(dump_content)
            print("Contact has been updated")
    else:
        print("Contact not found")

def delete():
    search_input = input("Enter the name of contact you want to delete : ")
    result = {}
    for contact in contacts:
        if search_input in contact["name"]:
            result = contact
    if len(result) > 0:
        file_name = search_input + ".json"
        path = os.path.join(project_path, file_name)
        os.remove(path)
        print("Contact has been deleted")
    else:
        print("Contact not found")

print("                          Welcome to your personal contact manager\nPlease select a number to choose an option:\n1) Add new contacts               2) View all contacts\n3) Search for a contact           4) Update a contact\n5) Delete a contact")
option = int(input("Number: "))
if option == 1:
    save_contact()
elif option == 2:
    list_of_contacts()
elif option == 3:
    search()
elif option == 4:
    update()
else:
    delete()