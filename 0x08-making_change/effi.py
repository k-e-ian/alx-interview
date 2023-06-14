#!/usr/bin/python3.8
'''
File: 0-making_change.py
'''


def makeChange(coins, total):
    '''Determine the fewest number of coins needed to meet a given amount total
    '''

    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize the count of coins used
    coin_count = 0

    # Iterate over each coin value
    for coin in coins:
        # Calculate how many times the coin can be used
        num_coins = total // coin

        # Increment the coin count
        coin_count += num_coins

        # Update the remaining total
        total -= num_coins * coin

        # If the total becomes zero, return the coin count
        if total == 0:
            return coin_count

    # If the total != zero, means the total cant be met by any combo of coins
    return -1
