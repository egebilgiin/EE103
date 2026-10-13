given_number = int(input("Type a number: "))

if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess_number = 1
    
    while guess_number**2 < given_number:
        guess_number += 1
        
    if guess_number**2 == given_number:
        print("Perfect Square!")
    else:
        print("It is not a perfect square.")


    