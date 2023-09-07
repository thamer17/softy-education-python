import json
with open(
    r"json\person.json", 
    "r"
) as json_file:
    content = json_file.read()
    #conversion from str to dict
    person = json.loads(content)
    print(person)
    