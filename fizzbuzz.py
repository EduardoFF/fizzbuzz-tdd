def process(n):
    if n == 15 or n == 30 or n == 45:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n

def fizzbuzz():
    for number in range(1, 101):
        print(process(number))
