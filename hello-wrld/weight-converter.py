weight = round(int(input('Weight: ')))
unit = input('(K)g or (L)bs? ')

if unit.upper() == 'L':
    print(f'Your weight: {weight * 0.45} kilos')
else:
    print(f'Your weight: {weight / 0.45} pounds')
