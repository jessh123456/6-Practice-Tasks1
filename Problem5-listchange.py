numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
location = numbers.index(353)
numbers.pop(location)
numbers.insert(location, 53)
print(numbers)
