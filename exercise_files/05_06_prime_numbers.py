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



def allPrimesUpTo(test_num):

    for num in range(1,test_num):
        for factor in range(2, num):
            if num % factor == 0:
                break         
        else:
            print(f'{num} is Prime')

      
    return 0



def main():
    '''
    main function
    '''
    allPrimesUpTo(100)




if __name__ == "__main__":
    main()
