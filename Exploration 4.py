print("----Grocery System----")
a = 0
b = 0
sum = 0
while True:
    item = input('Item:')
    unit = input('Enter the Unit:')
    a = int(unit)
    price = input('Enter the price: ')
    b = int(price)
    sum += a * b
    next_item = input('Is there another item? ')
    if next_item != 'Yes':
        break
print('Total Items purchased :', sum)
