# Authentication sathi auth('username','password') use karaicha
# website ssl certificate verify karat asel bt te skip karaiche asel tr verify=False use karaiche
# file upload karaiche asel tr files use karaiche

import requests

from utilities.endpointsConfigurationFile import *

"""config = getMethodEndpoint()

r = resources()

# config['API']['getEndpoint'] means [API] section madhla [getEndpoint] variable pahije
url = config['API']['getEndpoint'] + r.getBookResources

params = {"AuthorName": "Rahul Shetty2"}

response = requests.get(url, params=params, auth=HTTPDigestAuth)

value = response.json()

print(value)"""

# Authentication

config = getMethodEndpoint()

# rb means read mode

file = {"file": open("C:\\Users\\swapnil.bedse\\PycharmProjects\\pythonProject\\apiAutomation\\jsonFile.csv", 'rb')}
response = requests.get(config['API']['authenticationEndpoint'],
                        auth=('rahulshettyacademy', 'agfhjhff'),
                        verify=False,
                        files=file,
                        )
