#!/usr/bin/env python
# 02_07 Challenge
# 2024-02-09:geg
'''
LinkedIn Learning
Python Essential Training
Ryan Mitchell
Released: 1/25/2023

02 07 Challenge
'''

def factorial(num):
    '''
    Return the factorial of an integer
    '''
    if not isinstance(num, int):
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    # Use recursion to calculate factorial
    return num * factorial(num - 1)



def main():
    '''
    main function
    '''
    test = [5, 6, 0, -2, 1.2, 'spam spam spam spam spam spam']

    for num in test:
        num_factorial = factorial(num)
        if num_factorial:
            print(f'Factorial of {num} is {factorial(num)}')
        else:
            print(f'Could not calculate factorial of {num}')

if __name__ == "__main__":
    main()
