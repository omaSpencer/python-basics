names = ['John', 'Bob', 'Mary', 'Karen']
print(names[:3])
print(names[-1])
names[0] = 'Jon'
print(names)

numbers = [1, 5, 3, 6, 3, 7, 9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f'Largest number in list: {max}')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][2] = 999
print(matrix[1][2])
for row in matrix:
    for item in row:
        print(item)

numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(5))
print(5 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers_new = numbers.copy()
numbers_new.clear()
print(numbers_new, numbers)

list_with_duplicates = [1, 1, 3, 4, 5, 6, 7, 7]
for item in list_with_duplicates:
    if list_with_duplicates.count(item) > 1:
        list_with_duplicates.remove(item)
print(list_with_duplicates)
