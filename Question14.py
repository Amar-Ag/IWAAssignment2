import csv

def read_from_life(filename):
    """
    14. Write a function that reads a CSV file. It should return a list of
    dictionaries, using the first row as key names, and each subsequent
    row as values for those keys.
    For the data in the previous example it would return:
    [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
    'John', 'address': '54 Love Ave', 'age': 21}]
    """
    result_list = []
    with open(filename, mode='r') as inputFile:
        csv_reader = csv.DictReader(inputFile)
        for row in csv_reader:
            result_list.append(row)
    return result_list


print(read_from_life("Demo.csv"))
