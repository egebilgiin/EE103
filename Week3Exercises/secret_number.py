secretnum = 5
guess = int(input("Type a number."))
if guess > secretnum:
    print("Too high.")
elif guess < secretnum:
    print("Too Low.")
elif guess == secretnum:
    print("It is the secret number!")