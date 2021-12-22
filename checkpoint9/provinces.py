with open('provinces.txt') as text_file:
    providences = []
    for line in text_file:
        line = line.strip()
        providences.append(line)
        modified_list = line.replace('AB', 'Alberta')
    print(providences)
    print(f'Alberta occurs {modified_list.count("Alberta")} times in the modify list')