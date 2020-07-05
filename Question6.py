"""
6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""
nameToFind = "John"
sampleList = ['Ram', 'Hari', 'Sita', 'Ashim', 'Nhyu', 'Rajan', 'John']
flag = 0
for personName in sampleList:
    if personName == nameToFind:
        print(f"{nameToFind} found in index {sampleList.index(personName)}")
        flag = 1;

if flag == 0:
    print(f"{nameToFind} not found.")
