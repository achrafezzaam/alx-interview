#!/usr/bin/python3
''' Define the isWinner algorithm '''


def isWinner(x, nums):
    ''' Return the winner of the prime game '''
    if (x <= 0 or nums is None) or x != len(nums):
        return None

    score_player_1 = 0
    score_player_2 = 0

    new = [True for x in range(sorted(nums)[-1] + 1)]
    new[0], new[1] = False, False

    for i in range(2, len(new)):
        clean(new, i)

    for i in nums:
        if sum(new[0:i + 1]) % 2 == 0:
            score_player_1 += 1
        else:
            score_player_2 += 1

    if score_player_1 > score_player_2:
        return "Ben"

    if score_player_1 > score_player_2:
        return "Maria"

    return None


def clean(array, x):
    ''' Set the multiples of x to False '''
    for i in range(2, len(array)):
        try:
            array[i * x] = False
        except Exception as e:
            break
