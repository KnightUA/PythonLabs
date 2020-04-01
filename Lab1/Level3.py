def get_numeric(prompt):
    while True:
        try:
            res = float(input(prompt))
            break
        except (ValueError, NameError):
            print("Numbers only please!")
    return res


def get_char(prompt):
    while True:
        res = input(prompt)
        if len(res) != 1:
            print("Char must be!")
        return res


def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Incorrect operation!"


number_a = get_numeric("a = ")
number_b = get_numeric("b = ")
operation = get_char("Entry operation like +, -, * or /: ")

print(calculate(number_a,number_b,operation))
