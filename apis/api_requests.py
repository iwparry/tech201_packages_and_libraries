# API

# Application Programming Interface
# How software can communicate with one another

import requests
import json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# print(post_codes_req) # <Response [200]>
#
# print(post_codes_req.status_code) # 200 - everything is fine with the website
# print(post_codes_req.headers) # raw http headers (in a dictionary)
# print(post_codes_req.content) # raw content returned - in dict again
# print(post_codes_req.json()) # raw content in json format - easier for us to use
# print(type(post_codes_req.json())) <class 'dict'>

json_body = json.dumps({"postcodes":["LL55 1SH", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
print(post_multi_req.json())  # we use post go get specific data, which the server sends to us