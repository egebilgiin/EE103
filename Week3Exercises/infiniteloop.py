secretnum = 5
guess = int(input("Type a number."))
attempt = 0
flag = False
while secretnum != guess and attempt < 6:
    print("Try Again.")
    guess = int(input("Type a number."))
    attempt+=1
    if attempt >= 6:
        flag = True
    while flag:
        print("OH NOOO")

print("Congrats!")