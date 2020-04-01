from random import shuffle


def generate_list_of_numbers(size):
    numbers = list(range(0, 101))
    shuffle(numbers)
    return numbers[:size]

list_of_numbers = generate_list_of_numbers(25)

print("===== Initial =====")
print(list_of_numbers)

list_of_numbers.sort()
list_of_numbers.reverse()

print("===== Sorted =====")
print(list_of_numbers)

odd_indexes_list = []
for i in range(len(list_of_numbers)):
    if i % 2 == 1:
        odd_indexes_list.append(list_of_numbers[i])

print("===== Odd indexes =====")
print(odd_indexes_list)