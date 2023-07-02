#!/usr/bin/python3
'''
File: 0-prime_game.py
'''


def isWinner(x, nums):
    '''
    Determine the winner of the prime number game. '''

    def generate_primes(n):
        '''
        Generate list of prime numbs using the Sieve of Eratosthenes algo	 '''
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [num for num, is_prime in enumerate(primes) if is_prime]

    def get_round_winner(n):
        '''
        Determine the winner of a single round based on available prime nums
        '''
        primes = generate_primes(n)
        if len(primes) % 2 == 0:
            return 'Ben'
        return 'Maria'

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        round_winner = get_round_winner(n)
        if round_winner == 'Maria':
            maria_wins += 1
        elif round_winner == 'Ben':
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
