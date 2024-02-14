def sum_of_digits(num):
    return sum(map(lambda x: int(x), str(num)))

sum_num = 34524
result = sum_of_digits(sum_num)
print(result)
