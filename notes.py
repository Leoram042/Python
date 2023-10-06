"""
Syntax: {variable_name:.<number_of_after_decimal_digits>f}
"""
SAMPLE_FLOAT_VARIABLE = 10.123156
print(f"Printing a float variable with 4 decimals using f-string:{SAMPLE_FLOAT_VARIABLE:.4f}")

INT1 = 10
INT2 = 2

print(INT1 // INT2)  # Integer Division
print(INT1 / INT2)  # Float Division


LEAP_YEAR_TO_CHECK = 2000

"""
A year is a leap year if it is divisible by 400 or it is divisible by 4 and not by 100.
"""

LEAP_YEAR_STATUS = LEAP_YEAR_TO_CHECK % 400 == 0 or (
    LEAP_YEAR_TO_CHECK % 4 == 0 and LEAP_YEAR_TO_CHECK % 100 != 0
)
print(LEAP_YEAR_STATUS)
