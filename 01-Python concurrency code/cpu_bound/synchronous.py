# cpu_bound/synchronous.py
import time

def calculate(limit):
    a = [ i for i in range(limit)]
    b = [ i * i for i in range(limit)]

    result = sum(a)
    
    print("a: ", a)
    print("b: ", b)
    print("soma: ", result)
    return result

def find_sums(numbers):
    for number in numbers:
        print ("calculate:", number)
        calculate(number)
        print()

if __name__ == '__main__':
    #numbers = [5_000_000 + x for x in range(20)]

    numbers = [1 + x for x in range(4)]
    print("numbers: ", numbers)
    print()
    find_sums(numbers)
    
