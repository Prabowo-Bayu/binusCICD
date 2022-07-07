import requests

print("hello world")
print("I am Ironmand")

response = requests.get("https://google.com")

print (response.text)