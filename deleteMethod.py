import requests

response = requests.post("http://216.10.245.166/Library/DeleteBook.php",
                         json={"ID": "abcdefhh234"},
                         headers={"Content-Type": "application/json"}, )

value = response.json()

print(value)
