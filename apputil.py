import numpy as np


# update/add code below ...

def ways(n: int) -> int:
    """
    Returns the number of ways to make n cents using pennies (1 cent) and nickels (5 cents).
    """
    # For every possible number of nickels (from 0 up to n//5),
    # the remainder can be filled with pennies.
    return n // 5 + 1

# def ways_set(cents: int, coin_types=[1, 5]) -> int:
#     """
#     Return the number of ways to make 'cents' using the given coin_types.
    
#     Parameters
#     ----------
#     cents : int
#         The target amount in cents.
#     coin_types : list[int], optional
#         List of available coin denominations. Defaults to [1, 5].

#     Returns
#     -------
#     int
#         Number of ways to make 'cents' using the given coin types.
#     """
#     # Use dp: dp[i] = number of ways to make i cents
#     dp = [0] * (cents + 1) # Initialize dp array [0,0,...,0]
#     dp[0] = 1  # One way to make 0 cents (no coins)

#     # For each coin, update the dp
#     for coin in coin_types:
#         for amount in range(coin, cents + 1):
#             dp[amount] += dp[amount - coin]

#     return dp[cents]

import numpy as np

def lowest_score(names: np.ndarray, scores: np.ndarray) -> str:
    """
    Return the name of the student with the lowest score.
    """
    idx = np.argmin(scores)   # index of the lowest score
    return names[idx]

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

print(lowest_score(names, scores))

def sort_names(names: np.ndarray, scores: np.ndarray) -> list[str]:
    """
    Return a list of names sorted by descending score.
    """
    idx_sorted = np.argsort(scores)[::-1]  # indices sorted high→low
    return names[idx_sorted].tolist()
print(sort_names(names, scores))