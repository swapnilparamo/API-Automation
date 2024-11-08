# query parameter provide karnyastahi params

""" response retrieve karnyastahi text method...string return karel so tyala parse karaiche...
 but  reponse la directly parse karaiche asel tr reponse.json() method"""

# status code check karnyastahi respose.status_code method
# reponse body madhle headers check karnyastahi reponse.headers method
# reponse body madhle cookies check karnyastahi reponse.cookies method




import requests

response = requests.get("http://216.10.245.166/Library/GetBook.php",
                        params={"AuthorName": "Rahul Shetty2"}, )

"""value = response.text
print(type(value))
print(value)

value1 = json.loads(value)

print(type(value1))"""

value = response.json()
print(type(value))

status_code = response.status_code
print(status_code)

headers = response.headers
print("hearders are=", headers)
print(type(headers))

cookies = response.cookies
print(cookies)
print(type(cookies))
