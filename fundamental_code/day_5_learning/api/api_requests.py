# api requests

import requests

post_codes_req = requests.get("https://postcodes.io/postcodes/bn17fe")

print(post_codes_req) # Prints the response
print(post_codes_req.header) # Prints the headers
print(post_codes_req.contents) # gives json body as bytes (bytes are determined by wrapping in b')


print(post_codes_req.json()) # Prints dict
