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

'''
A year is a leap year if it is divisible by 400 or it is divisible by 4 and not by 100.
'''

LEAP_YEAR_STATUS = LEAP_YEAR_TO_CHECK % 400 == 0 or (
		LEAP_YEAR_TO_CHECK % 4 == 0 and LEAP_YEAR_TO_CHECK % 100 != 0
)
print(LEAP_YEAR_STATUS)

"""
In print statement,
	Default end parameter value is '\n' 
	Change end parameter value by end="" ("" means no space after print statement)
	Change sep parameter value by sep="," 
"""

for i in range(1, 6):
	print(i, end="")
# print(i, sep="")
print()

print('G', 'F', sep='', end='')
print('G')

print('09', '12', '2016', sep='-', end='\n')

print('leo', 'ram', sep='', end='@')
print('gmail.com')

print('Leoram')

"""
any returns True if any of the items is True
all returns True if all of the items are True
"""

n = int(input())
list_of_n = list(map(int, input().split()))  # maps the input elements by splitting it into a list of integers
print(n, list_of_n)

print(any([1 > 0, 1 == 0, 1 < 0]))

print(any([1 < 0, 2 < 1, 3 < 2]))

print(all(['a' < 'b', 'b' < 'c']))

print(all(['a' < 'b', 'c' < 'b']))

# print(all(int(i) > 0 for i in list_of_n) and any(str(j) == str(j)[::-1] for j in list_of_n))

print(all([int(i) > 0 for i in list_of_n]) and any([str(j) == str(j)[::-1] for j in list_of_n]))

"""
sorted function sorts the given input treating it as an iterable and returns the result in a list format
sorting is ascending by default
Syntax: sorted(<variable_name_of_value_to_be_sorted>, key = <function_to_sort_the array>, reverse = <bool_value>)
<variable_name_of_value_to_be_sorted> --> the value to be sorted
<function_to_sort_the_array> --> the sorting order must be given in the reverse order separated by commas
reverse --> True to sort it in the descending order
"""
input_string = "Sorting1234"

# Sort the string based on custom criteria
sorted_string = sorted(input_string, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))
print(sorted_string)

# Join the sorted characters to form the final string
result = ''.join(sorted_string)

print(result)
