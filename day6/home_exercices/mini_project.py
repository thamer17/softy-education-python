print("                          Welcome to your personal contact manager")
print("Please select a number to choose an option:\n1) Add new contacts               2) View all contacts\n3) Search for a contact           4) Update a contact\n5) Delete a contact")
option = int(input("Number: "))
import json
def add_new_contacts():
    new_contact = {"name": "", "phone number": "" , "email": ""}
    name = input("Enter a contact name: ")
    phone_number = int(input("Enter contact phone number: "))
    email = input("Enter a contact email: ")
    new_contact["name"] = name
    new_contact["phone number"] = phone_number
    new_contact["email"] = email
    with open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "r") as contacts_file:
        contacts_list = json.loads(contacts_file.read())
        contacts_list.append(new_contact)
    with open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "w") as contacts_file:    
        contacts_file.write(json.dumps(contacts_list))
def view_all_contacts():
    contacts_file = open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "r")
    content = contacts_file.read()
    print(content)
def search_for_a_contact():
    with open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "r") as contacts_file:
        contacts_list = json.loads(contacts_file.read())
    contactu = input("Enter a contact name: ")
    for contact in contacts_list:
        if contact["name"] == contactu:
            print(contact)
def update_a_contact():
    contact_name = input("Enter a contact name: ")
    print("Note: If you don't want to update some details, let it empty")
    new_name = input("Enter a new name: ")
    new_phone_number = input("Enter a new phone number: ")
    new_email = input("Enter a new email: ")
    with open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "r") as contacts_file:
        contacts_list = json.loads(contacts_file.read())
    for contact in contacts_list:
        if contact["name"] == contact_name:
            if len(new_name) > 0:
                contact["name"] = new_name
            if len(new_phone_number) > 0:
                contact["phone number"] = int(new_phone_number)
            if len(new_email) > 0:
                contact["email"] = new_email    
    with open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "w") as contacts_file:    
        contacts_file.write(json.dumps(contacts_list))
def delete_a_contact():
    contact_name = input("Enter a contact name: ")
    with open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "r") as contacts_file:
        contacts_list = json.loads(contacts_file.read())
    for contact in contacts_list:
        if contact["name"] == contact_name:
            contacts_list.remove(contact)
    with open(r"C:\Users\starinfo\Softy Education\day6\home_exercices\contacts.json", "w") as contacts_file:    
        contacts_file.write(json.dumps(contacts_list))
if option == 1:
    add_new_contacts()
elif option == 2:
    view_all_contacts()
elif option == 3:
    search_for_a_contact()
elif option == 4:
    update_a_contact()
else:
    delete_a_contact()

    
            









