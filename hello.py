import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print("Hello from my first backend project!")