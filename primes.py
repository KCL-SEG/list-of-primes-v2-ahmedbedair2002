"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    if number_of_primes <= 0:
        raise ValueError
        return list
    list_length = number_of_primes
    while list_length != 0:
        for x in range(2,count):
            if count % x == 0:
                break
        else:
            list.append(count)
            list_length -= 1
        count += 1
    return list
