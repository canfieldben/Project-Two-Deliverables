"""
When running this program, expect it to run many times before finding a value, this is because it is trying to find
which values give us an average profit higher than $1.7 which we found to be the highest possible profit with
our simulation
"""


from random import *
from math import *
i = 0
run_time = 0


def simulation(x, y, z, q):
    # Establishes the competitors prices and then assigns our prices based off the variables being passed into the function
    CB1 = 5.0
    CB2 = 5.0
    CA1 = x
    CA2 = y
    # Established the locations
    LA1 = z
    LA2 = q
    LB1 = 4
    LB2 = 8

    scores = []
    # Random starting location for our customers
    customer_location = uniform(0, 10)
    # Calculates the distance from each store based off their starting location
    distance_A1 = abs(customer_location - LA1)
    distance_A2 = abs(customer_location - LA2)
    distance_B1 = abs(customer_location - LB1)
    distance_B2 = abs(customer_location - LB2)
    # Calculates the scores for each store based of the location and the price
    A1_score = (10 - distance_A1 + 3 * (6 - CA1))
    A2_score = (10 - distance_A2 + 3 * (6 - CA2))
    B1_score = (10 - distance_B1 + 3 * (6 - CB1))
    B2_score = (10 - distance_B2 + 3 * (6 - CB2))
    # Finds the best score out of all of them
    best_score = max(A1_score, A2_score, B1_score, B2_score)
    # Adds up all of the scores
    total_score = A1_score + A2_score + B1_score + B2_score
    # Calculates the probability of each store
    prob_A1 = A1_score / total_score
    prob_A2 = A2_score / total_score
    prob_B1 = B1_score / total_score
    prob_B2 = B2_score / total_score

    # print(A1_score)
    # print(A2_score)
    # print(prob_A1)
    # print(prob_A2)

    # a random number between 0-1 that decides the the choice of the customer
    choice = uniform(0, 1)
    # algorithm that picks which store based of the two probabilities
    if choice < prob_A1:
        # print("A1")
        return CA1 - 2
    elif prob_A1 <= choice < (prob_A1 + prob_A2):
        # print("A2")
        return CA2 - 2
    elif (prob_A1 + prob_A2) <= choice < (prob_A1 + prob_A2 + prob_B1):
        # print("B1")
        return 0
    else:
        # print("B2")
        return 0


# function that runs the simulation to find the best profit and which values gave us that
# Note that it does not find the best average profit, but only the best profit that was achieved once!!!
def run_simulation():
    i = 0
    profit_dict = {}

    while i < 10000:

        # picks random values for price and location
        CA1 = uniform(2, 6)
        CA2 = uniform(2, 6)

        LA1 = uniform(0, 10)
        LA2 = uniform(0, 10)

        combined_numbers = str(CA1) + ',' + str(CA2) + ',' + str(LA1) + ',' + str(LA2)
        total = simulation(CA1, CA2, LA1, LA2)
        profit_dict[combined_numbers] = total

        i += 1

    best_combo = str(max(profit_dict, key=profit_dict.get))
    best_combo_list = (best_combo.split(','))

    final_CA1 = best_combo_list[0]
    final_CA2 = best_combo_list[1]
    final_LA1 = best_combo_list[2]
    final_LA2 = best_combo_list[3]

    # print(profit_dict)
    print(
        "CA1: " + final_CA1 + "\n" + "CA2: " + final_CA2 + "\n" + "LA1: " + final_LA1 + "\n" + "LA2: " + final_LA2 + "\n" + "Highest Profit Achieved: " + str(
            (profit_dict[max(profit_dict, key=profit_dict.get)])))

    return final_CA1, final_CA2, final_LA1, final_LA2


# Takes the values that gave us the best profit and runs those numbers many times to find the average profit with those values
def average_profit(x, y, z, q):
    i = 0
    total = 0
    while i < 100000:
        total += (simulation(x, y, z, q))
        i += 1
    return str(total/100000)

# the number being compared was the highest average, this number can be changed depending on the outcome you get each time
# note that if you make the number too high the simulation will run for ever trying to find an average higher
# $1.7 seems to be the highest average profit this simulation can find... however the program will still run potentially hundreds of times until it finds an average greater.


while i < 1.68:
    run_time += 1
    pass_list = run_simulation()
    i = float((average_profit(float(pass_list[0]), float(pass_list[1]), float(pass_list[2]), float(pass_list[3]))))
print("Average Profit with these values: " + str(i))
print("Simulation ran: " + str(run_time) + " times")

