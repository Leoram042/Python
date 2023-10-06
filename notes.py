"""
Syntax: {variable_name:.<number_of_after_decimal_digits>f}
"""
SAMPLE_FLOAT_VARIABLE = 10.123156
print(f"Printing a float variable with 4 decimals using f-string:{SAMPLE_FLOAT_VARIABLE:.4f}")

INT1 = 10
INT2 = 2

print(INT1//INT2) # Integer Division
print(INT1/INT2) # Float Division
