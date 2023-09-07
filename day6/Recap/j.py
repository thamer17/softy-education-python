import json
with open(r"C:\Users\starinfo\Softy Education\day6\Recap\data.json", 'r') as json_file:
    json_content = json_file.read()
    content = json.loads(json_content)
content["creation"] = 1991
print(content)
with open(r"C:\Users\starinfo\Softy Education\day6\Recap\data.json", 'w') as json_file:
    dump_content = json.dumps(content)
    json_file.write(dump_content)


