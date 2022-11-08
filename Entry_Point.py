# Entry Point in Python is used with __name__

def calculate_Area(side):
    return side * side


# From here python can start executing block of code
if __name__ == "__main__":
    square_Area = calculate_Area(4)
    print(square_Area)