"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

num1 = input("give me a number")
num1int = int(num1)

num2 = input("give me a second number")
num2int = int(num2)

if (num1int % num2int) == 0:
    print('the second number divides evenly into the first')
    
else:
    print('the second number doesnt divide evenly into tge first')
