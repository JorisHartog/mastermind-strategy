#!/usr/bin/env python3

## mastermind_strategy.py
# A simple script to test an algorithm for playing 6-color mastermind.
#
# Written by Joris Hartog, jorishartog<at>hotmail<dot>com
# https://github.com/JorisHartog

import itertools
from statistics import mean

def combinations(s):
    """Returns all combinations of a given set."""
    return [ ''.join(x) for x in itertools.permutations(s) ]

def try_permutation(_permutation, _solution):
    """Check how many colors are correct and how many are in the set."""
    correct = 0
    in_set = 0
    permutation = str(_permutation)
    solution = str(_solution)

    for i, color in enumerate(permutation):
        if solution[i] == color:
            solution = solution[:i] + ' ' + solution[i+1:]
            correct += 1

    for color in solution:
        if color in permutation:
            permutation.replace(color, '', 1)
            in_set += 1

    return (correct, in_set)

def possible(permutation, tries):
    """Returns true if the given permutation matches previous tries."""
    for t, a in tries:
        answer = try_permutation(t, permutation)
        if answer != a:
            return False
    return True

s = 'BWRGUY' # Black, White, Red, Green, blUe, Yellow

solutions = [a+b+c+d for a in s for b in s for c in s for d in s]
results = []

for solution in solutions:
    print(f'===== {solution} =====')
    solution_set = ''
    tries = []
    found = False
    while not found:
        try:
            color = s[len(tries)]
        except:
            assert len(solution_set) == 4
            color = 'foobar'
        _set = solution_set + color*(4 - len(solution_set))
        assert len(_set) == 4
        for permutation in [''.join(x) for x in itertools.permutations(_set)]:
            if possible(permutation, tries):
                answer = try_permutation(permutation, solution)
                tries.append((permutation, answer))
                print(f'{len(tries)}: {permutation}')
                if answer == (4, 0):
                    found = True
                    print(f'Found solution in {len(tries)} tries!')
                    results.append(len(tries))
                elif sum(answer) > len(solution_set):
                    solution_set += color*(sum(answer) - len(solution_set))
                break

print(f'Average tries: {mean(results)}')
print(f'Max tries: {max(results)}')
