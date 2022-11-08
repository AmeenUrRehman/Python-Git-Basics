# List in python can store different datatypes

# Make a list of groceries
Items = [ "Egg" , "Bread" , "Chips" , "Butter" , "Milk"]
print(Items)

print(Items[0])
print(Items[1])
print(Items[2])
print(Items[3])
print(Items[4])

Items[0] = "Dairy Milk"
print(Items)
Items.append("Coffee")
print(Items)
Items.pop()
print(Items)
Items.insert(2 , "Bingo")
print(Items)

# We can concatenate the list to list not alternatives of each other
Items2 = [ "Butter Nane" , "Biryani" , "Coca Cola"]
Concat_List = Items + Items2
print(Concat_List)

# To find the length
print(len(Concat_List))