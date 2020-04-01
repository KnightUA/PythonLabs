from math import sqrt

def string_to_number_list(input):
    is_correct_data = True

    items = input.split(",")
    for j in range(len(items)):
        try:
            items[j] = int(items[j])
        except (ValueError, NameError):
            is_correct_data = False
            break

    if not is_correct_data:
        return []

    return items


def get_fibonacci_numbers(numbers_list):
    fibonacci_numbers = []

    for number in numbers_list:
        if is_fibonacci_number(number):
            fibonacci_numbers.append(number)

    return fibonacci_numbers


def is_fibonacci_number(n):
   return True if sqrt(5 * (n ** 2) - 4) % 1 == 0 or sqrt(5 * (n ** 2) + 4) % 1 == 0 else False


numbers_list = string_to_number_list(input("Entry row of numbers split by ',':"))
print("===== Result =====")
print(get_fibonacci_numbers(numbers_list))