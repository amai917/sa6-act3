sort_strings = lambda lst: sorted(lst, key=lambda x: (len(x), x))

strings_list = ["elephant", "tiger", "lion", "ape", "bird", "lizard"]
sorted_list = sort_strings(strings_list)
print(sorted_list)
