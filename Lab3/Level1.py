from random import shuffle


def generate_list_of_numbers(size):
    numbers = list(range(0, 101))
    shuffle(numbers)
    return numbers[:size]


def get_numeric(prompt):
    while True:
        try:
            res = int(input(prompt))
            break
        except (ValueError, NameError):
            print("Numbers only please!")
    return res


def bias_list(list, step, count_of_bias_times):

    new_list = list

    for n in range(count_of_bias_times):
        print("Step %d" % (n + 1))
        new_list = new_list[-step:] + new_list[:-step]
        print(new_list)

    return new_list


list = generate_list_of_numbers(7)
step = get_numeric("Enter step:")
count_of_times = get_numeric("Enter count of times:")
print("===== Initial =====")
print(list)
print("===== Start Bias =====")
result = bias_list(list, step, count_of_times)
print("===== End Bias =====")
print(result)