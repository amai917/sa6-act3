def expo_map(num, n):
    return list(map(lambda x: x**n, num))

num_list = [1, 2, 3, 4, 5]
power = 2
powered_num = expo_map(num_list, power)
print(powered_num)
