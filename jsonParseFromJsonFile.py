# json file madhla data parse karnyastahi   load method....dictionary return karel

import json
import os

cwd = os.getcwd()
d2 = {}

with open(cwd + "\\jsonFile.csv") as f:
    dict_json = json.load(f)
    keys = dict_json.keys()
    print(dict_json)

    for key in keys:
        if key == "courses":
            values = dict_json[key]
            print(values)
            print(type(values))

            for value in values:
                keys1 = value.keys()
                if value.get("title") == "abc":
                    v1 = value.get("details")
                    k3 = v1.keys()
                    for k in k3:
                        d2[k] = v1[k]

print(d2)
