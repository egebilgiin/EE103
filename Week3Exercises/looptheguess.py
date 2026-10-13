secretnum = 5
guess = int(input("Type a number."))
while secretnum != guess:
    print("Try Again.")
    guess = int(input("Type a number."))
print("Congrats!")