Players_Goals = {
    "Messi" : 126 ,
    "Ronaldo" : 130 ,
    "Mbappa" : 100 ,
    "NeyMar" : 50 ,
}
print(Players_Goals)
print(Players_Goals["Messi"])

del Players_Goals["NeyMar"]
print(Players_Goals)

print("Messi" in Players_Goals)

for k , v in Players_Goals.items():
    print("Key:" , k , "Value : ", v)

# Tuples
Tuple_eg = ("Albert Einstein" , "Okay" , "Done")
print(type(Tuple_eg))
print(Tuple_eg)