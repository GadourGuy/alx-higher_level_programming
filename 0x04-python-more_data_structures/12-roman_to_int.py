#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10,
             'L': 50, 'C': 100, 'D': 500,
             'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman.keys():
            if (i + 1) < len(roman_string):
                if roman.get(roman_string[i]) < roman.get(roman_string[i+1]):
                    big = roman.get(roman_string[i+1])
                    result += (big - roman.get(roman_string[i]))
                    i += 1
                else:
                    result += roman.get(roman_string[i])
            else:
                result += roman.get(roman_string[i])
    return result
