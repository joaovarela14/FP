
def insertionSort(lst,key=lambda x: x):
    # Traverse elements starting at position 1
    for i in range(1, len(lst)):
        x = lst[i] 
        j = i - 1
        while j >= 0 and key(lst[j]) > key(x):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = x
    return



def main():
    lst0 = ["paulo", "augusto", "maria", "paula", "bernardo", "tito"]
    print("lst0", lst0)

    # sort in lexicographic order:
    lst = lst0.copy()
    insertionSort(lst)
    print("lst1", lst)
    assert lst == sorted(lst0)

    # sort by length (requires key= argument):
    lst = lst0.copy()
    insertionSort(lst, key=len)
    print("lst2", lst)
    assert lst == sorted(lst0, key=len)

    # sort by length, than lexicographic order:
    myorder = lambda s:(len(s), s)
    lst = lst0.copy()
    insertionSort(lst, key=myorder)
    print("lst3", lst)
    assert lst == sorted(lst0, key=myorder)

    print("All tests OK!")

if __name__ == "__main__":
    main()

