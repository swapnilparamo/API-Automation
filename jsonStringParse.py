# json string parse karnyastahi  loads method ...and dictionary return karelimport json


import json

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'

dict_json = json.loads(courses)

keys = dict_json.keys()

for key in keys:
    if key == "languages":
        list = dict_json.get(key)
        print(list[0])
