#Albert
'''
This function takes no parameters. It asks the user "how much change is owed"
and retuns the minimum amount of coins needed. The function will re-prompt the
user if a number less than 0 is entered
'''
 
def calculate(change=None):

#Asks for input(change that is owed) rounds the float to two decimal places.
   
    change = round(float(input("How much change is owed? ")), 2)
#A loop that reprompts user if the number entered is less than 0
    while change < 0:
        change = round(float(input("How much change is owed? ")), 2)
        if change >= 0:
            break
#changes the float into a integer to avoid error
    changes = int(change * 100)
    coins = 0


#Floor divide the integer change by the coin(25, 10, 5, 1)and add the number
#to the variable(coin). Then divide the number by coin(25, 10, 5, 1) and set
#the change = to the remainder.

    coins += changes // 25
    changes = changes % 25
           
    coins += changes // 10
    changes = changes % 10

    coins += changes // 5
    changes = changes % 5

    coins += changes // 1
    changes = changes % 1
 

#To make the output grammatically correct, if the number of coins equals 1, it
#will print out you need 1 coin. If it is larger or equal to 0, it will print
#out coins.

    
    if coins > 1 or coins == 0:
        print("You need {0} coins".format(coins))
    else:
        print("You need {0} coin".format(coins))

calculate()
