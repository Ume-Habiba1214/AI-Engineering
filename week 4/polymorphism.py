class Animal:
    def speak(self):
        print("Animal makes a sound")



class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


dog = Dog()
cat = Cat()
def make_sound(animal):
        animal.speak()

make_sound(dog)
make_sound(cat)