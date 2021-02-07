import random
import csv
import re


def calculate_roll(calculation):
    # check the passed string to make sure it is properly formatted
    pattern = re.compile('\d+[d]\d+[x]?\d*')
    result = pattern.match(calculation)
    if result is None:
        raise Exception('function calculate_coins must receive a format [int]d[int]x[int]')

    # determine the count of dice
    diepos = calculation.find("d", 0)
    diecount = int(calculation[0:diepos])

    # determine the multiplier. If there is no multiplier, this value will be -1 and will be skipped
    multpos = calculation.find("x", 0)
    if multpos > -1:
        diesize = int(calculation[diepos + 1:multpos])
    else:
        diesize = int(calculation[diepos + 1:])

    coins = 0
    count = 1

    # for each die, randomly select a number between 1 and the number of faces of the die
    while count <= diecount:
        coins += random.randint(1, diesize)
        count += 1

    # if the multiplier position is not a positive number, there is no multiplier, skip this
    if multpos > 0:
        multiplier = int(calculation[multpos + 1:])
        coins *= multiplier
    return coins


def load_flat_table(file):
    """General utility which will read a structure table and return a list of dictionaries where each dictionary
    represents a row from the table"""
    with open(file, mode='r', encoding='utf-8-sig') as csvfile:
        contents = csv.reader(csvfile)
        linecount = 0
        table = []  # will hold the values to be returned
        headers = []  # headers from the first row of the table
        for row in contents:
            # if processing the first row, low those values to a special list of headers to be used to dictionary keys
            if linecount == 0:
                for item in row:
                    headers.append(item.lower())
            else:
                # all rows after the first should be processed the same
                columncount = 0
                new_row = {}
                for item in row:
                    if item != "":
                        # if the value is numeric, cast it as an integer
                        if str(item).isnumeric():
                            new_row[headers[columncount]] = int(item)
                        else:
                            new_row[headers[columncount]] = item
                    columncount += 1
                table.append(new_row)
            linecount += 1
    return table

def filter_table_by_cr(table, cr=0):
    """General utility that takes a list of dictionary entries, likely processed from a CSV, and limits the list
    by the specified challenge rating (CR) for each row. This function assumes that each dictionary has the following
    two keys: cr-min and cr-max. If it doesn't, those records will simply be dropped from the table"""
    filtered_table = []
    for row in table:
        if 'cr-min' and 'cr-max' in row:
            if row['cr-min'] <= cr <= row['cr-max']:
                filtered_table.append(row)

    return filtered_table


def load_cr_based_table(file, cr=0):
    """General utility which will read a structure table and return a list of dictionaries where each dictionary
    represents a row from the table. This function assumes that the table will have two columns with the headings
    cr-min and cr-max. It will filter the results based on the cr passed so as to only return table values based
    on the cr rating"""
    temp_table = load_flat_table(file)
    table = filter_table_by_cr(temp_table, cr)

    return table

if __name__ == "__main__":
    mytable = load_cr_based_table('../tables/treasure_hoard.csv',2)
    print(mytable)
