"""
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""

listOfFriendsAndColleagues = []
initialId = id(listOfFriendsAndColleagues)
print("Initial Id of the object:", initialId)

# Appending names of friends and colleagues
listOfFriendsAndColleagues.append("Nhyu Joshi")
listOfFriendsAndColleagues.append("Arjun Saud")
listOfFriendsAndColleagues.append("Khushi Shrestha")
listOfFriendsAndColleagues.append("Dikpal Poudel")
listOfFriendsAndColleagues.append("Khem Sharma")

# Check if there is any difference after append
postAppendId = id(listOfFriendsAndColleagues)
print("Id of the list after appending names of colleagues and friends:", postAppendId)
if initialId == postAppendId:
    print("There is no change in object Id after append.")
else:
    print("There is a change in object Id after append.")

# Sorting and check if there is any difference in id after sorting
listOfFriendsAndColleagues.sort()
postSortId = id(listOfFriendsAndColleagues)
print("Id of the list after sorting.", id(listOfFriendsAndColleagues))
if initialId == postSortId:
    print("There is no change in object Id after sorting.")
else:
    print("There is a change in object Id after sorting.")

print(f"First Item of the list:{listOfFriendsAndColleagues[0]}")
print(f"Second Item of the list:{listOfFriendsAndColleagues[1]}")
