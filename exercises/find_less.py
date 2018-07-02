l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_lis = []

def less_five (lis):
    for num in lis:
        if num < 5:
            new_lis.append(num)
            new_lis.sort()
        else:
            continue
    print(set(new_lis))

less_five(l)
            
