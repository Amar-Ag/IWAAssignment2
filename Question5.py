"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""
personalDetails = ('Amar', 'Agrawal', '21')

peopleList = []
peopleList.append(personalDetails)

friendOne = ('Nhyu', 'Joshi', '20')
friendTwo = ('Arjun', 'Saud', '21')
colleagueOne = ('Dikpal', 'Poudel', '38')
colleagueTwo = ('Khem', 'Sharma', '42')

peopleList.append(friendOne)
peopleList.append(friendTwo)
peopleList.append(colleagueOne)
peopleList.append(colleagueTwo)

print("Original List:", peopleList)
peopleList.sort(key=lambda x: x[0])
print("Sorting the list by first name:", peopleList)
peopleList.sort(key=lambda x: x[1])
print("Sorting the list by last name:", peopleList)
peopleList.sort(key=lambda x: x[2])
print("Sorting the list by age:", peopleList)
