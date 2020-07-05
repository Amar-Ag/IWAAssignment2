def binary_search(sorted_list, item):
    """
    9. Write a binary search function. It should take a sorted sequence and
    the item it is looking for. It should return the index of the item if found.
    It should return -1 if the item is not found.
    """
    first = 0
    last = len(sorted_list) - 1
    flag = False
    print("Sorted input list:", sorted_list)
    while (first <= last and not flag):
        mid = (first + last) // 2
        if sorted_list[mid] == item:
            flag = True
            return mid
        else:
            if item < sorted_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1


demoList = [9, 4, 3, 2, 5, 6, 8, 7]
print(binary_search(sorted(demoList), 10))
print(binary_search(sorted(demoList), 6))
