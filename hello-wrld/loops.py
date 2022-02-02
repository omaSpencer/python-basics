i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

for item in 'Python':
    print(item)

for item in range(0, 10, 2):
    print(item)

prices = [10, 20, 30]
total_price = 0
for price in prices:
    total_price += price
print(f"Total: {total_price}")

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
