#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    else:
        rom_dictionary = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        d = [rom_dictionary[c] for c in roman_string]
        result = 0
        for i in range(len(d)):
            result += d[i]
            if d[i - 1] < d[i] and i != 0:
                result -= (d[i - 1] + d[i - 1])
        return (result)
