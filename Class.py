class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def work_humans_do(self):
        if self.occupation == "Player":
            print("Human is a Player in Sports hahaha")
        elif self.occupation == "Actor":
            print("Human is a Actor in Movies hahhaha")

    def speaks(self):
        print(self.name+ " says How are you!!")

check = Human("Tom" , "Actor")
check.work_humans_do()
check.speaks()