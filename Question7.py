"""
7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""
personalDetails = ('Amar', 'Agrawal', 21)

peopleList = []
sumOfAge = 0
countAge = 0
peopleList.append(personalDetails)

friendOne = ('Nhyu', 'Joshi', 'None')
friendTwo = ('Arjun', 'Saud', 21)
colleagueOne = ('Dikpal', 'Poudel', 38)
colleagueTwo = ('Khem', 'Sharma', 42)

peopleList.append(friendOne)
peopleList.append(friendTwo)
peopleList.append(colleagueOne)
peopleList.append(colleagueTwo)

for record in peopleList:
    if record[2] == "None":
        pass
    else:
        sumOfAge += record[2]
        countAge += 1

averageAge = sumOfAge / countAge
print("Entered list:", peopleList)
print("Average Age:", averageAge)

for record in peopleList:
    if record[2] == "None":
        print(record[0], "- Age not entered.")
    else:
        if record[2] > averageAge:
            print(record[0], "- Old")
        else:
            print(record[0], "- Young")
