import random

print("Welcome to the Lottery numbers generator.")
number = input("Please enter how many random numbers would you like to have: ")


def loto(n):
    new = []
    for x in range(0, n):
        ran = random.randint(1, 40)
        if ran not in new:
            new.append(ran)
        else:
            ran = random.randint(1, 40)
            new.append(ran)
    return new


for i in range(1, 100):
    print loto(number)



