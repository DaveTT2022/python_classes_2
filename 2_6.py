import json
import yaml

txt_json = {
    "firstName": "Rack",
    "lastName": "Jackon",
    "gender": "man",
    "age": 24,
    "address": {
        "streetAddress": 126,
        "city": "San Jone",
        "state": "CA",
        "postalCode": 394221
    },
    "phoneNumbers": [
        { "type": "home", "number": 7383627627 }
    ]
}

with open("text.json", "w") as json_info:
    json.dump(txt_json, json_info, indent = 4)

# JSON to txt

with open("text.json", "r") as JSON_info:
    with open("text.txt", "w") as txt_file:
        txt_file.write(JSON_info.read())

# JSON to yaml

with open("text.json", "r") as JSON_info:
    with open("text.yaml", "w") as yaml_file:
        yaml_file.write(yaml.dump(json.load(JSON_info), sort_keys = False))

# Yaml to JSON

with open("text.yaml", "r") as yaml_info:
    with open("text_2.json", "w") as JSON_file:
        JSON_file.write(json.dumps(yaml.safe_load(yaml_info), indent = 4))

# Yaml to txt

with open("text.yaml", 'r') as yaml_info:
    with open("text_2.txt", 'w') as text_file:
        text_file.write(str(yaml.safe_load(yaml_info)))
