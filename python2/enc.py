print("encapsulation")
#oops concepts ..



     
drinks = {
 'black russian': {'vodka', 'kahlua'},
 'white russian': {'cream', 'kahlua', 'vodka'},
 'manhattan': {'rye', 'vermouth', 'bitters'},
 'screwdriver': {'orange juice', 'vodka'},
 'martini': {'vodka', 'vermouth'}
}
for name , contents in drinks.items():
    if  contents & {'vermouth'}:
        print(name)






