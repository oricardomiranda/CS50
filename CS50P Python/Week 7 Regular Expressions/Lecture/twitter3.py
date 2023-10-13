import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE): #parenthesis will catch the match. ?: will prevent that
	print(f"Username:", matches.group(1)) #First group is for www