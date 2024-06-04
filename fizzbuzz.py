def process(n):
    if n % 3 == 0:
        return "Fizz"
    return n

def fizzbuzz():
    for number in range(1, 101):
        print(process(number))
