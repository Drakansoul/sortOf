def sortOf(sortList):
    # check with the user if the list is sorted
    sorted = input("Is the list sorted? (Y/n): ")
    # if not sorted try again
    if (sorted == "n"):
        sortOf(sortList)
    return sortList

if __name__=="__main__":
    listToSort = [1,2,3,"foo","bar"]
    sortedList = sortOf(listToSort)
    print(sortedList)