# The sandwich maker 
import pyinputplus as pyip
import time
from tabulate import tabulate

def write(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

print('='*30)
print('Welcome To Sandwich Maker Store')
print('='*30)

# Make dictionaries of prices(in Dollars)
bread_types = {'wheat': 1, 'white': 1, 'sourdough': 1.5}
protein_types = {'chicken': 2.75, 'turkey': 1.95, 'ham': 1.5, 'tofu': 3}
cheese_types = {'cheddar': 1, 'swiss': 1.25, 'mozzarella': 1.5}
optional_item_types = {'mayo': 2, 'mustard': 1.75, 'lettuce': 1, 'tomato': 1}

# Main Programme
write('\n=== Bread Types ===')
bread_menu = [f'{bread.capitalize()} - ${price}' for bread, price in bread_types.items()]
bread_choice = pyip.inputMenu(bread_menu, numbered=True)

write('\n=== Protein Types ===')
protein_menu = [f'{protein.capitalize()} - ${price}' for protein, price in protein_types.items()]
protein_choice = pyip.inputMenu(protein_menu, numbered=True)

write('\n=== Cheese ====')
want_cheese = pyip.inputYesNo('Do you want cheese? [y/N]: ')

if want_cheese == 'yes':
    write('\n=== Cheese Types ===')
    cheese_menu = [f'{cheese.capitalize()} - ${price}' for cheese, price in cheese_types.items()]
    cheese_choice = pyip.inputMenu(cheese_menu, numbered=True)
else:
    cheese_choice = 'none'

want_optional_items = pyip.inputYesNo('Do you want optional items? [y/N]: ')
if want_optional_items == 'yes':
    write('\n=== Optional Items ===')
    optional_menu = [f'{item.capitalize()} - ${price}' for item, price in optional_item_types.items()]
    optional_choice = pyip.inputMenu(optional_menu, numbered=True)
else:
    optional_choice = 'none'

write('\n=== Sandwiches Number ===')
sandwiches_number = pyip.inputInt('How many sandwiches do you want: ', min=1)

write('\n=== Summary of Items ===')

# Extract choices and calculate prices
bread_item = bread_choice.split(' - $')[0].lower()
bread_price = bread_types[bread_item]

protein_item = protein_choice.split(' - $')[0].lower()
protein_price = protein_types[protein_item]

if want_cheese == 'yes':
    cheese_item = cheese_choice.split(' - $')[0].lower()
    cheese_price = cheese_types[cheese_item]
else:
    cheese_item = 'none'
    cheese_price = 0

if want_optional_items == 'yes':
    optional_item = optional_choice.split(' - $')[0].lower()
    optional_price = optional_item_types[optional_item]
else:
    optional_item = 'none'
    optional_price = 0

# Calculate total
total_per_sandwich = bread_price + protein_price + cheese_price + optional_price
total_cost = total_per_sandwich * sandwiches_number

# Create order summary
order_data = [
    ['Bread', bread_item.capitalize(), f"${bread_price:.2f}"],
    ['Protein', protein_item.capitalize(), f"${protein_price:.2f}"],
    ['Cheese', cheese_item.capitalize(), f"${cheese_price:.2f}"],
    ['Optional', optional_item.capitalize(), f"${optional_price:.2f}"],
    ['', 'QUANTITY', sandwiches_number],
    ['', 'TOTAL', f"${total_cost:.2f}"]
]

print(tabulate(order_data, headers=['Item', 'Choice', 'Price'], tablefmt='grid'))
