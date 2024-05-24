#!/usr/bin/env python
# 06_04 Challenge
# 2024-05-24:geg
'''
LinkedIn Learning
Python Essential Training
Ryan Mitchell

06 04 Challenge

Given a function triangle(num) that returns the number of positions in a traingle

triangle(4) = 10

#
##
###
####

Create a new function square(num) that returns num ** 2

'''


def triangle(num):
    '''
    
    '''
    if num == 1:
        return num
    return num + triangle(num - 1)


def square(num):
    '''
    
    '''
    return triangle(num) + triangle(num - 1)




def main():
    '''
    main function
    '''

    for num in range(2,10):
        square_num = square(num)
        print(f'Square of {num} is {square_num}')




if __name__ == "__main__":
    main()
