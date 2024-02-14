def intersection(ls1, ls2):
    return list(filter(lambda x: x in ls1, ls2))

list1 = [1, 2, 3, 4, 5]
list2 = [1, 4, 5, 7, 8]
intersected_list = intersection(list1, list2)
print(intersected_list)
