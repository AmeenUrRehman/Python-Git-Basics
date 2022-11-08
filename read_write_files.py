# It write the line on given file txt

f = open("Notes.txt" , "w")

# a is used to append the new line in previous lines.

r = open("Notes.txt" , "a")

# To read lines
m = open("Notes.txt" , "r")

f.write("\n I hate Python like breath haha.")

print(f.read())

f.close()