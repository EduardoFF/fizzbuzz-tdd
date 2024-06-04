def process(n):
    if n == 1:
        return 1
    return 42

def fizzbuzz():
    for number in range(1, 101):
        print(process(number))
