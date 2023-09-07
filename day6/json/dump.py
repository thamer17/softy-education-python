import json
pet ={"name": "Pascal", 
    "type": "Dog", 
    "age": 4}

with open(r"json\dump.json", "w") as dump_file:
    # conversion from dict to str
    dump_pet = json.dumps(pet)
    dump_file.write(dump_pet)
    print("File has been created!")