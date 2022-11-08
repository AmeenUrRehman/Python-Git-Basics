number = [2,4,6,8,13,17,5,4]
odd = []
for num in number:
    if num%2 != 0:
        odd.append(num)
print(odd)

# List Comprehensions
odd = [num for num in number if num%2 != 0]
print(odd)

