#divisors

def divisor(num):
    d_list = []
    for x in range (1, num + 1):
        if num % x == 0:
            d_list.append(x)
        else:
            continue
    print(d_list)

og_num = input("What number would you like to find the multiples of?: ")
print()
divisor(int(og_num))
