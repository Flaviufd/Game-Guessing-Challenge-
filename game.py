import random

random_number = random.randint(1, 100)

rules = """ This is the game rules
1. If guess is out of bounds, say "OUT OF BOUNDS";
2. On first turn, if guess is within 10 of number, return "WARM!", else "COLD!";
3. On subsequent turns, if guess is closer to number than previous guess, return "WARMER!", else "COLDER!";
4. When guess equals number, tell "correct" and number of guesses!"""

print(rules)


guesses_list = [0]
number_from_player = 0

while True:
    number_from_player = int(input("Enter your guess between 1 and 100: "))
    
    if number_from_player < 1 or number_from_player > 100:
        print("OUT OF BOUNDS")
        continue
        
    if number_from_player == random_number:
        print(f"Congratulations! You have guessd the number {random_number} correctly in {len(guesses_list)} guesses!")
        break
    
    guesses_list.append(number_from_player)
    
    if guesses_list[-2]:
        if abs(random_number - number_from_player) < abs(random_number - guesses_list[-2]):
            print("WARMER!")
        else:
            print("COLDER!")
    else:
        if abs(random_number - number_from_player) <= 10:
            print("WARM!")
        else:
            print("COLD!")