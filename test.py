num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in num_list:
    del num_list[i]
    print(num_list)
    if len(num_list) == 1:
        break
