def get_char(prompt):
    while True:
        res = input(prompt)
        if len(res) != 1:
            print("Char must be!")
        return res


def get_boolean(prompt):
    while True:
        res = input(prompt)
        if res.lower() == "true" or res == "1":
            return True
        elif res.lower() == "false" or res == "0":
            return False
        else:
            print("Wrong value!")


looking_symbol = get_char("Enter looking symbol:")
is_case_important = get_boolean("Is case type important (Write one of 'True' or 'False'; '1' or '0'):")
count_of_looking_symbols = 0

if not is_case_important:
    looking_symbol.lower()

with open('level3_test.txt') as inp:
    for line in inp:
        line = line.rstrip('\n')
        last_symbol = line[-1]
        if not is_case_important:
            last_symbol = last_symbol.lower()

        if last_symbol == looking_symbol:
            count_of_looking_symbols += 1

print("Count of looking symbols is %d" % count_of_looking_symbols)