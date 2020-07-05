"""

"""


def findTriplets(demoArray):
    flag = False
    length = len(demoArray)
    outputList = []
    for i in range(0, length - 2):
        # running 2nd loop so that the same elements are not compared
        for j in range(i + 1, length - 1):
            # running 3nd loop so that the same elements are not compared
            for k in range(j + 1, length):

                if (demoArray[i] + demoArray[j] + demoArray[k] == 0):
                    intermediatelist = [demoArray[i], demoArray[j], demoArray[k]]
                    outputList.append(intermediatelist)
                    flag = True

    # If no triplet with 0 sum
    # flag in array
    if (flag == False):
        print("No such triplets exist.")
    else:
        print(outputList)


inputArray = [-25, -10, -7, -3, 2, 4, 8, 10]
findTriplets(inputArray)
