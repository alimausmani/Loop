

#     Now, we will change the previous game a little. We only checked whether the number given by the user is equal to the input number or not.
#     Now, we will also tell the user if the number given by the user is greater or smaller than the input number.
#     If the user gives 4 as a number then we will check if 4 is less than 5 or not so it's true then we will print "Number entered by you entered is small, try one more time ".
#     We will again take input from the user. If the user gives 7 as a number then we will check if 7 is less than 5 or not so it is False then we will print "Number entered by you entered is greater, try one more time ".
#     If the user gives 5 as input then this number is equal to the given number then we will print "Wow you guessed the correct number".
#     User will keep on guessing until all the chances are finished.
# If we will give such types of hints to the user, it will become easier for him to solve the question.


# a=1
# while a<=5:
#     num=int(input("please enter the number:-"))
#     if num==5:
#         print("wow,you win the game")
#     if num%5==0:
#         break
#     elif num<5:
#         print("number entered by you is smaller than 5")
#     elif num>5:
#          print("number entered by you is greater than 5")
#          a=a+1
#     else:
#         print("game over")