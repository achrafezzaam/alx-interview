#!/usr/bin/python3
''' Solve the N Queens leetcode '''


def scroll(n, i=0, a=[], b=[], c=[]):
    ''' Find the possible positions for the queens '''
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from scroll(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def queens(n, i=0, output=[]):
    ''' Test all the possible positions for the queens in a nxn size board '''
    for elem in scroll(N, 0):
        for solution in elem:
            output.append([i, solution])
            i += 1
        print(output)
        i = 0
        output = []


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    N = int(sys.argv[1])
    queens(N)
