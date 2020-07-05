def is_prime(number):
    """ 8. Write a function, is_prime, that takes an integer and returns True if
        the number is prime and False if the number is not prime."""
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


inputNumber = int(input("Enter any number:"))
if is_prime(inputNumber):
    print(f"{inputNumber} is prime.")
else:
    print(f"{inputNumber} is not prime.")
