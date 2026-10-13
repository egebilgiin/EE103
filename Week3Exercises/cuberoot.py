given_number = int(input("Type an integer number: "))
target = abs(given_number)
guess = 0
while guess**3 < target:
    guess += 1
if guess**3 != target:
    print("it is not a perfect cube.")
else:
    if given_number < 0:
        guess = -guess
    print("The cube root of", given_number, "is", guess)