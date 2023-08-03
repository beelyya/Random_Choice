from random import randint

user_choice = int(input("Choose number:"))
pc_choice = randint(1,100)

if user_choice == pc_choice:
    print("You won")
elif user_choice > pc_choice:
    print("Lower! Computer choose:", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer choose:", pc_choice)

