import requests


browse = requests.get("https://nairaland.com")
print(browse.text)

with open("nairaland.html", "w") as mysite_file:
    mysite_file.write(browse.text)