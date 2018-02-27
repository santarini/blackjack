import random

def Roll():
    WhiteBalls = random.sample(range(1,70), 5)
    PowerBall = random.sample(range(1,27), 1)
    WhiteBalls.sort()
    print(WhiteBalls)
    print(PowerBall)
Roll()
