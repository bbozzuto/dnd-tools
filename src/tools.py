import random

def calculate_coins(calculation):
    diepos = calculation.find("d", 0)
    diecount = int(calculation[0:diepos])

    multpos = calculation.find("x", 0)
    diesize = int(calculation[diepos + 1:multpos])

    multiplier = int(calculation[multpos + 1:])
    coins = 0
    count = 1
    while count <= diecount:
        coins += random.randint(1, diesize) * multiplier
        count += 1
    return coins
