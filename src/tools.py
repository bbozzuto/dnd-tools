import random
import csv


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


def load_table(file):
    """General utility which will read a structure table and return a list of dictionaries where each dictionary
    represents a row from the table"""
    with open(file, mode='r', encoding='utf-8-sig') as csvfile:
        contents = csv.reader(csvfile)
        linecount = 0
        table = {}
        headers = []
        for row in contents:
            if linecount == 0:
                for item in row:
                    headers.append(item)
            else:
                columncount = 0
                key = ""
                for item in row:
                    if columncount == 0:
                        key = item
                        table[key] = {}
                    else:
                        if item != "":
                            table[key][headers[columncount]] = item
                    columncount += 1
            linecount += 1
    return table


if __name__ == "__main__":
    mytable = load_table('../tables/coins.csv')
    print(mytable)
