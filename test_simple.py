from fizzbuzz import process

def test_process_42():
    assert( process(42) == "Fizz")

def test_process_1():
    assert( process(1) == 1)

def test_multiples_of_three():
    assert process(3) == "Fizz"
    assert process(4) != "Fizz"
    assert process(33) == "Fizz"

def test_multiples_of_five():
    assert process(5) == "Buzz"
    assert process(10) == "Buzz"
