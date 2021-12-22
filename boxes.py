from math import ceil

def number_of_boxes(num_items, items_per_box):
	return ceil(items / items_per_box)
	
items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

print(f'With {items} items, packing {items_per_box} items per box, you need {number_of_boxes(items, items_per_box)} boxes')