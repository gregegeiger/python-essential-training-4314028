#!/usr/bin/env python
# 04_06 Challenge
# 2024-02-15:geg
'''
LinkedIn Learning
Python Essential Training
Ryan Mitchell
Released: 1/25/2023

04 06 Challenge
Given ascii art encode into a list of tuples



'''

def encodeString(stringVal):
    '''
    Given a string return a list of tuples
    AAAAABBBBAAA => [('A', 5), ('B', 4), ('A', 3)]
    This is called Run Length Encoding

    Parameters: 

    Returns: List of 2 element tuples
    '''
    code_list = []

    last_character = stringVal[0]
    char_count = 1

    for index in range(0, len(stringVal)):
        # examine the character at index position
        index_character = stringVal[index]

        # Check the character at index
        # If it matches last_character just increment the character count
        if index_character == last_character:
            # If it matches last_character just increment the character count
            char_count += 1
        else:
            # If does not match
            # Add a tuple from prior run
            code_list.append((last_character, char_count))
            # Change the last_character to character at this index
            last_character = index_character
            # Reset the character count
            char_count = 1
        
    # Add last tuple
    code_list.append((last_character, char_count))

        
    return code_list



def decodeString(encodedData):
    '''
    Given a list of tuples print the resulting string
    [('A', 5), ('B', 4), ('A', 3)] => AAAAABBBBAAA
    '''
    # Iterate through list
    for char_run in encodedData:
        run_length = char_run[1]
        while run_length > 0:
            print(char_run[0], end='')
            run_length -= 1
        
    return None

def main():
    '''
    main function
    '''

    art = '''



                                   %%%%%%%%%%%%%%%%%%%                              
                            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                        %%%%%%%%                         %%%%%%%%                   
                    %%%%%%%                                   %%%%%%                
                  %%%%%%                                         %%%%%%             
               %%%%%%                                               %%%%%           
              %%%%%                                                   %%%%%         
            %%%%%                                                       %%%%%       
           %%%%                 %%%%%              %%%%%                  %%%%      
          %%%%                 %%%%%%%            %%%%%%%                  %%%%     
         %%%%                  %%%%%%%            %%%%%%%                   %%%%    
        %%%%                   %%%%%%%            %%%%%%%                    %%%%   
        %%%%                    %%%%%              %%%%%                     %%%%   
       %%%%                                                                   %%%%  
       %%%%                                                                   %%%%  
       %%%%                                                                   %%%%  
       %%%%                                                      %%%%        %%%%   
        %%%%       %%%%%%                                        %%%%%       %%%%   
        %%%%         %%%%                                       %%%%        %%%%    
         %%%%         %%%%                                     %%%%         %%%%    
          %%%%         %%%%%                                  %%%%         %%%%     
           %%%%%         %%%%%                             %%%%%         %%%%%      
            %%%%%          %%%%%%                        %%%%%          %%%%        
              %%%%%           %%%%%%%               %%%%%%%           %%%%%         
                %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
                  %%%%%%%                                        %%%%%              
                     %%%%%%%                                 %%%%%%%                
                         %%%%%%%%%                     %%%%%%%%%                    
                              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                       %%%%%%%%%%%%                                 



    '''


    code_list = encodeString(art)

    decodeString(code_list)




if __name__ == "__main__":
    main()
