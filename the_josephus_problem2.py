num = 42

list_of_numbers = []
for i in range(1, num+1):
    list_of_numbers.append(i)

print(list_of_numbers)

death = 3
for i in list_of_numbers:
    if i == num:
        if i == death:
            print("XX")
        else:
            print(i)

    elif i < 10:
        if i == death:
            print(f"XX", end=" - ")
        else:
            print(f"0{i}", end=" - ")

    elif i % 10 == 0:
        if i == death:
            print("XX")
        else:
            print(i)

    else:
        if i == death:
            print("XX")
        else:
            print(f"{i}", end=" - ")

