import random
dicerolling = True
while dicerolling:
    print(random.randint(1,6))
    playagain = input("do you want roll again [y/n]:")
    if playagain == "y":
        continue
    else:
        print("game over")
        break