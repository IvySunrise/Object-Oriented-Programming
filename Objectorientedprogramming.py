class Enemy():
    def __init__(self, name, prod_number):
        self.prod_number = prod_number
        self.name = name
        print("This is " + self.name + " ,you don't like his face very much")
        
    def prod(self, prod_number):
        if self.prod_number == 4:
            print("You can no longer prod " + self.name + ", he wants to fight")
        else:
            print("You have prodded the enemy")
            if self.prod_number <= 2:
                print(self.name + " thinks your attempt to annoy them is cute")
            else:
                print(self.name + " is irritated with you.")

    def increase(self):
        self.prod_number += 1
