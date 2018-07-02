
def even_odd (num):
    if num % 4 == 0:
        print(f"{num} is a multiple of four")
        if num % 2 == 0:
            print(f"{num} is a even number")
        else:
            print(f"{num} is an odd number")

number = input("What number would you like to check?: ")
print()
even_odd(int(number))

