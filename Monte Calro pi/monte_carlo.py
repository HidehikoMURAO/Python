import random
import math


def monte_carlo(count):
    ok = 0
    for _ in range(count):
        x = random.random()
        y = random.random()
        if (x * x) + (y * y) <= 1:
            ok += 1
    return 4 * ok / count

print('For    100 {0}' .format(monte_carlo(100)))
print('For   1000 {0}' .format(monte_carlo(1000)))
print('For  10000 {0}' .format(monte_carlo(10000)))
print('For 100000 {0}' .format(monte_carlo(100000)))
