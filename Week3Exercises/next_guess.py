cube = 27.0           # Aradığımız sayıyı koda gömüyoruz (hardcode)
epsilon = 0.01        # Kabul edilebilir hata payı
num_guesses = 0       # Ana Bell'in hız ölçme sayacı
guess = cube / 2.0    # Aramaya sayının yarısından başlıyoruz

while abs(guess**3 - cube) >= epsilon:
    guess = guess - (((guess**3) - cube) / (3 * guess**2))
    num_guesses += 1  # Her döngü turunda sayacı artır

print('num_guesses =', num_guesses)
print(cube, 'sayısının yaklaşık küp kökü:', guess)