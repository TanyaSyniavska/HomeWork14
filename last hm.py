import random 
print(dir(random))

menu_items = input('Введіть список страв, розділених комами: ')
menu_items = menu_items.split(',')
print(menu_items)

print('—--Кафе “У Монті”---')

total_price = 0
for item in menu_items:
    price=random.randint(20,300)
    total_price =  total_price + price
    print(f'{item.strip().capitalize()}....... {price}грн')
print(f'Всього...... {total_price}грн')