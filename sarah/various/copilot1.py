# convert a roman numeral to an integer
# 1. create a dictionary of roman numerals and their values
# 2. create a function to convert a roman numeral to an integer
# 3. create a function to convert an integer to a roman numeral

# 1. create a dictionary of roman numerals and their values
roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# 2. create a function to convert a roman numeral to an integer
def roman_to_int(roman):
    '''convert a roman numeral to an integer'''
    # initialize the integer
    integer = 0
    # loop through the roman numeral
    for i in range(len(roman)):
        # if the current roman numeral is less than the next roman numeral
        if i < len(roman) - 1 and roman_numerals[roman[i]] < roman_numerals[roman[i + 1]]:
            # subtract the current roman numeral from the integer
            integer -= roman_numerals[roman[i]]

        # otherwise
        else:
            # add the current roman numeral to the integer
            integer += roman_numerals[roman[i]]

    # return the integer
    return integer




# 3. create a function to convert an integer to a roman numeral
def int_to_roman(integer):

    # initialize the roman numeral
    roman = ''


    # loop through the roman numerals
    for numeral in sorted(roman_numerals, key=roman_numerals.get, reverse=True):
        # while the integer is greater than or equal to the current roman numeral
        while integer >= roman_numerals[numeral]:
            # add the current roman numeral to the roman numeral
            roman += numeral
            # subtract the current roman numeral from the integer
            integer -= roman_numerals[numeral]

    # collapse the repeated roman numerals
    roman = roman.replace('IIII', 'IV')
    roman = roman.replace('XXXX', 'XL')
    roman = roman.replace('CCCC', 'CD')
    roman = roman.replace('VIV', 'IX')
    roman = roman.replace('LXL', 'XC')
    roman = roman.replace('DCD', 'CM')


    # return the roman numeral
    return roman

# test the functions
print(roman_to_int('MCMXCIX'))
print(int_to_roman(1999))

