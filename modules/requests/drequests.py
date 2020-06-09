import requests

url="https://www.google.com/"

ret=requests.get(url)

print(ret)
print(dir(ret))
print(help(ret))
print(ret.text)
print(ret.status_code) //returns status code
print(ret.ok) //prints ok if status code is less 400
print(ret.headers) //prints header info

payload={'page': 2,'count': 25}
ret=requests.get('https://httpbin.org/get',params=payload)
print(ret.url)  //prints url

for post we use data keyword for payload
payload={'firstname': 'dheeraj', 'lastname': 'chopra'}
ret=requests.post('https://httpbin.org/post', data=payload)
ret_dict=ret.json()
print(ret_dict)

Testing authentication
ret=requests.get('https://httpbin.org/basic-auth/dheeraj/chopra', auth=('dheeraj','chopra'))

Checking timeout
ret=requests.get('https://httpbin.org/delay/6', timeout=3)


Download an image
import requests
url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
ret=requests.get(url)
with open('google.png','wb') as f:
  f.write(ret.content)