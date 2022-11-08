""" We are going to write function for addition of elements in the list"""

def calculate_items(exp):
    total = 0
    for items in exp:
        total = total + items
    return total

Items = [ 2 , 4 , 4 , 5]
Total = calculate_items(Items)
print(Total)