BASE_URL ="https://jsonplaceholder.typicode.com/"

###gets item from dictionary and reads JSON
import requests
response = requests.get(f"{BASE_URL}/posts/1")
print(response.status_code)

data = response.json()
response.raise_for_status()
print(data["title"])
print(data)

###get query paramaters
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}

)
posts = response.json()
print(len(posts))
for post in posts[:3]:
    print(post["title"])

###request fails 404
response = requests.get(f"{BASE_URL}posts/9999")
print(response.status_code)

###POST to send data
new_post = {"title": "Mi primer post", "body": "Hola API", "userId": 1}
response = requests.post(
    f"{BASE_URL}posts",
    json=new_post
)
print(response.status_code)
print(response.json())
