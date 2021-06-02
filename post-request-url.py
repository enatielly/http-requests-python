#Post Request in Python, route to POST:
url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)

#Comparing the URL from the response object of the GET and POST:
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

#compare the POST and GET request body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

#view the form as well:
r_post.json()['form']

