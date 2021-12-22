from math import pi

def main():
    radius = get_radius()
    height = get_height()
    # for i in radius:
    #     efficency = compute_volume(float(i), float(j)) / compute_surface_area(float(i), float(j))
    #     print(f'{efficency:.1f}')

def compute_volume(radius, height):
    return pi * (radius * radius) * height

def compute_surface_area(radius, height):
    return 2 * pi * radius * (radius + height)

def get_radius():
    radius = []
    with open('can_sizes.txt') as txt:
        for i in txt:
            clean = i.strip()
            items = clean.split()
            if len(items) == 5:
                items.pop(1)
            radius.append(items[1])
        return radius

def get_height():
    height = []
    with open('can_sizes.txt') as txt:
        for i in txt:
            clean = i.strip()
            items = clean.split()
            if len(items) == 5:
                items.pop(1)
            height.append(items[2])
        return height

main()