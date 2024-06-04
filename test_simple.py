from fizzbuzz import process, get_fizzbuzz_list

def test_process_42():
    assert process(42) == "Fizz"

def test_process_1():
    assert process(1) == 1

def test_multiples_of_three():
    assert process(3) == "Fizz"
    assert process(4) != "Fizz"
    assert process(33) == "Fizz"
    assert process(99) == "Fizz"

def test_multiples_of_five():
    assert process(5) == "Buzz"
    assert process(10) == "Buzz"

def test_multiples_of_3_and_5():
    assert process(15) == "FizzBuzz"
    assert process(30) == "FizzBuzz"
    assert process(45) == "FizzBuzz"
    assert process(60) == "FizzBuzz"
    assert process(75) == "FizzBuzz"
    assert process(90) == "FizzBuzz"

def test_fizzbuzz_islist():
    assert isinstance(get_fizzbuzz_list(),list)

def test_fizzbuzz_list_has_len_100():
    assert len(get_fizzbuzz_list()) == 100

def test_fizzbuzz_list_first_15():
    L = get_fizzbuzz_list()
    assert L[:15] == [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz']
