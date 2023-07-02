#!/usr/bin/python3
'''
File: 0-prime_game.py
'''


def isWinner(x, nums):
    '''
    Determine the winner of the prime number game.
    '''
    def is_prime(num):
        '''
        Check if a number is prime.
        '''
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(is_prime(i) for i in range(2, n + 1))

        # Maria wins if the number of primes is odd
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
