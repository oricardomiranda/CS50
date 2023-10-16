import re
import sys

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("Valid")
    else:
        print("Invalid")

# Validate an IPv4 address. Input str. Output True or False
# Numbers 0 to 255 as #.#.#.#
def validate(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$" #3 times the first pattern

    if re.match(pattern, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
