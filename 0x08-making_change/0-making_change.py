#!/usr/bin/python3
''' Define makeChange function '''


def makeChange(coins, total):
    ''' The number of coins needed to get total result '''
    if total <= 0:
        return 0
    coins.sort()
    i = len(coins) - 1
    count = 0
    while i >= 0:
        while total >= coins[i]:
            total -= coins[i]
            count += 1
        i -= 1
    if total == 0:
        return count
    return -1
