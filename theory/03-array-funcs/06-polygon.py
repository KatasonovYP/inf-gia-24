def process_number(num):
    squared = num ** 2
    subtracted = squared - 10
    return subtracted

numbers = [1, 2, 3, 4, 5]
new_numbers = map(process_number, numbers)

print(sorted(new_numbers))