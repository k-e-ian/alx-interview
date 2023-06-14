#!/usr/bin/python3.8
'''
File: 0-making_change.py
'''


def makeChange(coins, total):
    '''Determine the fewest number of coins needed to meet a given amount total
    '''

    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed
    min_coins = [float('inf')] * (total + 1)

    # Base case: Zero coins needed to make a total of 0
    min_coins[0] = 0

    # Iterate over each coin value
    for coin in coins:
        for value in range(coin, total + 1):
            # Determine the minimum between the current minimum and the minimum
            min_coins[value] = min(min_coins[value],
                                   1 + min_coins[value - coin])

    # If the min num of coins needed for the total is inf, cant be met
    if min_coins[total] == float('inf'):
        return -1

    # Return the minimum number of coins needed for the total
    return min_coins[total]
