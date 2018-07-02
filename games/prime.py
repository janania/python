


def isprime(num):
    if num % 2 == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



number = int(input("Please enter the number you would like to validate: "))
prime_num = isprime(number)
print(f"The given number {number} is {prime_num}")



def isprimetwo(start, end):
    for x in range(start, end):
        if isprime(x):
            print(x)

start = int(input("What is your starting number?: "))
end = int(input("What is your ending number?: "))

isprimetwo(start, end)





# print("The Prime Numbers are...")

#sleep(1)

#sleep(1)

#print("Thank you for using the Prime Number Generator! \nPlease visit us again :)")

#start = int(input("What is your starting number?: "))
#end = int(input("What is your ending number?: "))


