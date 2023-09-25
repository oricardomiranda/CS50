filename = input("File name: ")

filename = str.strip(filename)
filename = str.lower(filename)

match filename:
	case _ if ".gif" in filename:
		print("image/gif")
	case _ if ".jpg" in filename:
		print("image/jpeg")
	case _ if ".jpeg" in filename:
		print("image/jpeg")
	case _ if ".png" in filename:
		print("image/png")
	case _ if ".pdf" in filename:
		print("application/pdf")
	case _ if ".txt" in filename:
		print("text/plain")
	case _ if ".zip" in filename:
		print("application/zip")
	case _:
		print("application/octet-stream")