soldiers = int(input("Type the numbers of soldiers: "))

i = 1
prev_pow_2 = 0
while True:
    pow_2 = pow(2, i)
    if soldiers == pow_2:
        result = pow_2
        break
    elif soldiers < pow_2:
        result = prev_pow_2
        break
    prev_pow_2 = pow_2
    i += 1

#  W(n) = 2l + 1
survive_position = 2 * (soldiers - result) + 1
print("survive_position:", survive_position)
