#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
# 1 Instantiate the Cat object with 3 cats
cat = Cat('tom',7)
cat1 = Cat('jerry',5)
cat2 = Cat('spike',12)
# 2 Create a function that finds the oldest cat


def age(*args):
    return max(*args) 
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'the max age of cat is{age(cat.age,cat1.age,cat2.age)}')


