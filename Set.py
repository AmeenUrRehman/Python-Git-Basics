# Set is an unordered collection of unique elements

basket = {"Apple" , "Mango" , "Banana", "Watermelon" , "Apple"}
print(type(basket))
print(set(basket))

print(basket.add("Orange"))
print(basket)

# Frozen set is a type set which doesn't allow any adding or removing from the original set with its unique values

fs = frozenset(basket)
print(fs)

# It shows error as it's not allowed to add or remove elements in frozenset
# print(fs.add("Pinapple"))

# Set Operations
x = {"a" , "b" , "c"}
y = {"l" , "m" , "a"}
print(x|y)
print(x&y)
print(x<y)
print(x==y)
print(x-y)

