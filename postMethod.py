# request body provide karnyastahi json
# headers provide karnyastahi headers
# cookies provide karnyastahi cookies..dictionay format madhe ghyaiche

import json

import requests

response = requests.post("http://216.10.245.166/Library/Addbook.php",
                         json={"name": "abcdef",
                               "isbn": "abcdefhh",
                               "aisle": 234,
                               "author": "ghijkl"
                               },
                         headers={"Content-Type": "application/json"}
                         , )

value1 = response.text
print(type(value1))
value2 = json.loads(value1)
print(type(value2))

value = response.json()
print(type(value))

print(value)
