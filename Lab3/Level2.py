is_input = True

list = []

while is_input:
    value = input()
    try:
        if int(value) == 0:
            is_input = False
        else:
            list.append(value)
    except (ValueError, NameError):
        list.append(value)

print("Inserted list:")
print(list)
list.reverse()
print("Reversed list:")
print(list)