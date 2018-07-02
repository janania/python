def fibanacci(limit):
    previous = 0
    current = 1
    temp = None

    while current < limit:
        temp = current
        current = current + previous
        previous = temp
        print(previous)

fibanacci(100)
