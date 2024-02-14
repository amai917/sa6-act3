def find_maximum(num, compare):
    max = num[0]
    for number in num[1:]:
        max = compare(max, number)
    return max

greater = lambda a, b: a if a > b else b

num_list = [3,6]
max_num = find_maximum(num_list, greater)
print(max_num)
