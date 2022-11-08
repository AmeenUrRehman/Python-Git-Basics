# Exceptions are the errors detected at the time when the program execute

x = int(input("Enter the Number: "))
y = int(input("Enter the 2nd Number: "))
try :
    z = int(x) / int(y)
except Exception as e:
    print("Exception occured: " ,e)
    z = None
print("Divion is: " , z)

