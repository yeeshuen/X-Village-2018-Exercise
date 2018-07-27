class Animal :
    feet_number = 4
    
    def shout(self):
        print("Hello ! I'm Animal.")

class Dog(Animal) :
    pass

dog = Dog()

print(dog.feet_number)
dog.shout()
