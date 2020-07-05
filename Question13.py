def write_to_file(fileName, tupleList):
    """
    Write a function to write a comma-separated value (CSV) file. It
    should accept a filename and a list of tuples as parameters. The
    tuples should have a name, address, and age. The file should create
    a header row followed by a row for each tuple. If the following list of
    tuples was passed in:
    [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
    it should write the following in the file:
    name,address,age
    George,4312 Abbey Road,22
    """
    with open(fileName + '.csv', 'wt') as f:
        f.write("name,address,age\n")
        for record in tupleList:
            f.write(f"{record[0]},{record[1]},{record[2]}\n")


inputName = str(input("Enter a filename:")) or "Demo"
demoTuple = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21), ('Ram', 'Teku', 26)]
write_to_file(inputName, demoTuple)