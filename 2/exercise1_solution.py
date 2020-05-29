# an example solution for exercise 1, session 2

my_list = [1,5,3,7,10,11,45,2,14]

print("My list is {}".format(my_list))

for item in my_list:
    if item > 10:
        print("The number is over 10!")
    elif item == 10:
        print("The number is 10!")
    else:
        print("Small number!")
