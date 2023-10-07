def main():
	greeting = input("Greeting ").strip()
	print(f"${value(greeting)}")

def value(greeting):
    if greeting.lower() == "hello" or greeting.lower() == "hello, newman":
        return 0
    elif greeting.lower()[0] == "h":
    	return 20
    else:
        return 100

if __name__ == "__main__":
	main()


