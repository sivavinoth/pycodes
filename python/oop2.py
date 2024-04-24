class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

cat = Cat('tom', 7)
cat1 = Cat('jerry', 5)
cat2 = Cat('spike', 12)

def age(*args):
    return max(*args)

print(f'the max age of cat is{age(cat.age, cat1.age, cat2.age)}')

 










