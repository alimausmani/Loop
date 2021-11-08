

# Now, we will make a game using loops. We will call this game a guessing game.
#     In this game we take any number, let us suppose this number is number 5.
#     After this we take any number as an input from the user between 1 to 10. The user tries to guess this number.
#     Suppose the user gives 3as an input. We will then check if 3 is equal to 5 or not?
#     3 is not equal to 5 so we will ask the user for another input.
#     Now, we will check if that number is equal to 5 or not.
#     User will get 5 chances to guess.
# If he guessed right within the 5 chances he wins and if he guesses wrong then loses the game.
# Hint :
# Study about break statement`` in python.


# import random
# guesses=1
# number=random.randint (1,100)
# guess=int(input("guess a number between 1,100::-"))
# while guess!=number:
#     if guess < number:
#         print("your guess was too low")
#         guess=int(input("please guess again"))
#         guesses=guesses+1
#     elif guess>number:
#         print("your guess was too high")
#         guess=int(input("please guess again"))
#         guesses=guesses+1
#         print()
#         print("congratulation,you guessed the number")
#         break
# else:
#        print("you guessed wrong")




# import random

# number=random.randint(1,99)

# guess=int(input("enter an integer from 1 to 99::-"))
# while number!=guess:
#     if guess < number:
#         print("your guess was too low")
#         guess=int(input("enter an integer from 1 to 99:
#     elif guess>number:
#         print("your guess was too high")
#         guess=int(input("enter an integer from 1 to 99::-"))
#     else:
#         print("congratulations you guessed the number")
#         break
