import re

url = input("URL: ")

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) #substitute. do each test case at a time do you can debug
print(f"Username: {username}")