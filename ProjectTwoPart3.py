import random

def getExpectedProfit():
    # loc is location of the shop
    locA1= 2.6
    locA2=5.5
    locB1=4
    locB2= 8
    #cost of coffee for each shop
    costA1= 3.75
    costA2= 4.25
    costB1= 5
    costB2= 5
    # cost to make coffee
    coffeeCost = 2
    # starting profit at 0
    profit = 0
    # trials
    for i in range (1000000):
        #generate random number for customer location
        customer = random.random() * 10
        #scores for each shop
        scoreA1 = 10-(abs(customer-locA1))+3*(6-costA1)
        scoreA2= 10-(abs(customer-locA2))+3*(6-costA2)
        scoreB1=10-(abs(customer-locB1))+3*(6-costB1)
        scoreB2=10-(abs(customer-locB2))+3*(6-costB2)
        # probabilities for each shop
        probA1= scoreA1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        probA2= scoreA2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        probB1= scoreB1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        probB2= scoreB2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        #the choice of the customer
        choice = random.random()
        # if customer chose one of our shops, it would add the profit made from the cup of coffee to profit
        # if customer chose competitor shop, it would just set picking that shop to 1
        if choice < probA1:
            profit = profit + (costA1 - coffeeCost)
            pickA1 = 1
        elif probA1 <= choice < (probA1 + probA2):
            pickA2 = 1
            profit = profit + (costA2 - coffeeCost)
        elif (probA1 +probA2) <= choice < (probA1 + probA2 + probB1):
            pickB1 = 1
        else:
            pickB2 = 1
    # average profit
    profit = profit / 1000000
    # printing it to screen
    print("Expected profit is", profit)

getExpectedProfit()


