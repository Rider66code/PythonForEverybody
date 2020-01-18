from random import randrange

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

d1 = Dog("Astro")

d1.feed()

#There’s a better way to invoke a superclass’s method. Unfortunately, the implementation of python in our ActiveCode windows doesn’t support it, so we aren’t using it here. In that alternative method, we would call super().feed(). This is nice because it’s easier to read, and also because it puts the specification of the class that Dog inherits from in just one place, class Dog(Pet). Elsewhere, you just refer to super() and python takes care of looking up that the parent (super) class of Dog is Pet.
