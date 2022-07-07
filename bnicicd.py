import requests
from datetime import datetime
print("hello world")
print("I am Ironman")
response = requests.get("https://google.com")

waktu = datetime.now()

with open("tempResponse/"+str(waktu)+".txt", "w") as f:
    f.write(response.text)
