from utils import greeting, send_message, find_max

message = greeting('Hi there')
print(message)
send_message()

numbers = [1, 2, 3, 4, 5, 6, 7]
maximum = find_max(numbers)
print(f'Largest number in list: {maximum}')
