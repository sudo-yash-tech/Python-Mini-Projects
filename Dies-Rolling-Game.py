import random

while True:
    choice = input("Roll the Dies (y/n): ").lower()
    if choice == "y":
        dies1 = random.randint(1,6)
        dies2 = random.randint(1,6)
        print(f"({dies1}, {dies2})")
    elif choice == "n":
        print("Thanks For Playing the Game!!!")
        break
    else:
        print("Invalid Choice!!!")