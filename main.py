with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_quantity = int(file.readline())
        ingredient = []
        for _ in range(ingredient_quantity):
            ingr = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingr
            ingredient.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[dish_name] = ingredient

print(f'cook_book = {cook_book}')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for element in cook_book.get(dish):
                if element.get('ingredient_name') not in shop_list.keys():
                    ingr = {}
                    ingr.update({'measure': element.get('measure')})
                    ingr.update({'quantity': int(element.get('quantity')) * person_count})
                else:
                    past_meaning = shop_list.get(element.get('ingredient_name')).get('quantity')
                    ingr.update({'quantity': int(element.get('quantity')) * person_count + past_meaning}) 
                shop_list.update({element.get('ingredient_name'): ingr})
    print(f'shop_list: {shop_list}')


get_shop_list_by_dishes(['Омлет', 'Пирог'], 5)

line_count = ['1.txt', '2.txt', '3.txt']   
l_count = {}
for file in line_count:
    with open(file, 'rt', encoding='utf-8') as f: 
        count = f.read().count('\n') + 1
    l_count[file] = count
l_count = dict(sorted(l_count.items(), key=lambda item: item[1]))
print(l_count)


for element in l_count.items():
    with open(element[0],'rt', encoding='utf-8') as f:
        with open('4.txt', 'a', encoding='utf-8') as new_file:
            new_file.write(element[0] + '\n')
            new_file.write(str(element[1]) + '\n')
            new_file.write(f.read() + '\n')
            print()
