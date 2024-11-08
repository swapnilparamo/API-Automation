"""same authentication multiple requests sathi asel tr pratyek req madhe auth=('uname','pwd') aiwaji global authentication
use karaiche .....same for headers and cookies


url hit kelya nantr tya url la hit karaicha pahije other url la redirect  hot asel and ti url hit zalya nantr main url hit hot asel
.....tewa redirect hotai ka te check karnyastahi response.history method and tewa status code 301 asel means redirect hotai

url hit zalya ir req send kelya nantr nantr reponse retrive waila 5-6 secands lagat astil but tyacha aata code execute zala tr
 respons blanck bhetel.....ha pblm solve karnyasathi ...timeout=10 sec....means req send kelya natr 10 sec wait karel mg
  res retrive karel


"""

import requests

se = requests.session()
se.auth = auth = ('uname', 'pwd')

cookies = {"cookie_name": "cookie_value"}
se.cookies.update(cookies)

# ithe req .get aiwaji se.get ghetle

response = se.get("url")

# redirect and timeout

response = requests.get("url", timeout=10)
print(response.history)
