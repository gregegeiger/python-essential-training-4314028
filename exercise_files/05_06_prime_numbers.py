#!/usr/bin/env python
# 05_06 Challenge
# 2024-03-06:geg
'''
LinkedIn Learning
Python Essential Training
Ryan Mitchell
Released: 1/25/2023

05 06 Challenge

Write a function that returns a list of all primes up to a given number.

For each number, in order to determine if it is prime, take the following steps:

Find the square root of the number
Find all the primes up to that square root
Test to see if any of those primes are divisors
If a number has no prime divisors, it is prime!


'''



def allPrimesUpTo(max_num):
    '''Print all prime numbers up to the max_num provided
    
    '''
    # Create a list of the primes that you discover - seed it with 2
    found_primes = [2]
    for num in range(3,max_num):
        for prime in found_primes:
            if num % prime == 0:
                print(f'{num} in not prime because {prime} is a factor')
                break
        else:
            pass
        for factor in range(prime, int(num ** 0.5) +1):
            if num % factor == 0:
                break         
        else:
            print(f'{num} is prime')
            found_primes.append(num)

      
    return found_primes



def main():
    '''
    main function
    '''
    found_primes = allPrimesUpTo(100)
    print(found_primes)




if __name__ == "__main__":
    main()
