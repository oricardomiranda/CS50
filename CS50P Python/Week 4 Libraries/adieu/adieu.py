import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ").strip()
        name_list.append(name)
    except EOFError:
        print("Adieu, adieu, to", p.join(name_list))
        break