def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f'Reversed: {fruit_list}')
    fruit_list.append('orange')
    print(f'Appended: {fruit_list}')
    i = fruit_list.index('apple')
    fruit_list.insert(i, 'cherry')
    print(f'Cherry: {fruit_list}')
    fruit_list.remove('banana')
    print(f'No banana: {fruit_list}')
    bye = fruit_list.pop()
    print(f'Pop: {fruit_list} and poped: {bye}')
    fruit_list.sort()
    print(f'Sorted: {fruit_list}')
    fruit_list.clear()
    print(f'Cleared: {fruit_list}')
    
main()