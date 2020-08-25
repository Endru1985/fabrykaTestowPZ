#BIBLIOTEKA REQUESTS:

#przykład 1

import requests

r = requests.get('https://fabrykatestow.pl/')

print(r)

#przykład 2

import requests

post = requests.post('http:/httpbin.org/post')
put = requests.put('http:/httpbin.org/put')
delete = requests.delete('http:/httpbin.org/delete')

print(post, put, delete)

#przykład 3

paramtetres = {'key1':'value1', 'key2':'value2'}

r = requests.get('https://fabrykatestow.pl', params=paramtetres)
print(r.url)
print(r.text)
print(r.encoding)
