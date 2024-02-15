#!/usr/bin/env python
# 03_06 Challenge
# 2024-02-14:geg
'''
LinkedIn Learning
Python Essential Training
Ryan Mitchell
Released: 1/25/2023

03 06 Challenge
Without using the int class to convert a string hexidecimal to
a base 10 for strings up to three characters.
Handle incorrect characters.

'''

def hexToDec(hexNumbers, hexstring):
    '''
    Return a decimal integer when the string hexadecimal value
    is converted to base 10
    '''
    decimal_result = 0
    # Index into string to return one character slice
    for string_index in range(0, len(hexstring)):
        # Check for invalid character
        if hexstring[string_index] in hexNumbers:
            # Convert the single hex character slice into decimal and add to result
            decimal_result += hexNumbers[hexstring[string_index]]
            if string_index < len(hexstring) - 1:
                decimal_result *= 16
        else:
            return None
        
    return decimal_result



def main():
    '''
    main function
    '''

    # Create a dictionary of hexidecimal characters

    hexNumbers = {
        '0':0
        ,'1':1
        ,'2':2
        ,'3':3
        ,'4':4
        ,'5':5
        ,'6':6
        ,'7':7
        ,'8':8
        ,'9':9
        ,'A':10
        ,'B':11
        ,'C':12  
        ,'D':13
        ,'E':14
        ,'F':15             
    }
    
    # Test strings to run
    text_strings = [
        'A'
        ,'0'
        ,'1B'
        ,'3C0'
        ,'A6G'
        ,'ZZTOP'

    ]

    for hexstring in text_strings:
        decimal_result = hexToDec(hexNumbers, hexstring)
        if decimal_result:
            print(f'Hexidecimal string {hexstring} converts to {decimal_result}')
        else:
            print(f'Hexidecimal string {hexstring} is invalid')


if __name__ == "__main__":
    main()
