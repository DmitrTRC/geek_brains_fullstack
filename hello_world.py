def my_filter(array):
    return [x for x in array if not x % 2]


def average(array):
    return sum(array) / len(array)


def greeting(name):
    print(f'Hello {name} , glad to see you!')


print(average([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(my_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
greeting(input('Enter your name ->'))
