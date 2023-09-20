def roman_to_int(s: str) -> int:
    # use a dictionary to store the roman numerals and their values
    romans = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50, 
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    total = 0
    prev_val = 0

    # iterate backwards through the string
    for char in s[::-1]:
        # save the value of the char
        val = romans[char]

        # this helps us convert things like IV
        if val < total:
            total -= val
        # this helps us convert things like II
        else:
            total += val
            prev_val = val

    return total

print(roman_to_int("XIIV"))