#HTTP Request & Response Service:
url_get='http://httpbin.org/get'

#Create a Query string:
payload={"name":"Joseph","ID":"123"}

#Passing the dictionary payload to the params parameter of the get() function:
r=requests.get(url_get,params=payload)

#Print out URL, see name and values:
r.url

#There is no request body:
print('request body:', r.request.body)

#Print out status code:
print(r.status_code)

#View response text:
print(r.text)

#Look at the Content type:
r.headers['Content-Type']

#Returns a Python dict:
r.json()

#Key args has the name and values:
r.json()['args']


