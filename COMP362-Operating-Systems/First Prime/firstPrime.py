'''
"7427466391.com" the name of the website

Python code for finding the first 10 digit prime in the digits of Euler's e

By : Maxwell Scharkopf
'''
from decimal import Decimal, getcontext
"""
In my calculate_e_log I set the min value for this percision test. I then use 
Taylor series expansion to find the value of e. This expansion can be represented
as 1 + 1/1! + 1/2! + 1/3! + ... 1/n!. Once our term is small enough we break and 
return the value of e.
"""
def calculate_e_log(precision):
    getcontext().prec = precision # Set decimal precision
    e = Decimal(1)                # Set e to 1 since it starts with 1
    term = Decimal(1)             # Set first term is the series
    min_term = Decimal(10) ** (-precision) # Smallest value measured

    # Calculate Taylor series expansion of e
    for i in range(1, precision):
        term /= i                 # Each term is the last divided by i
        e += term                 # Current sum of e 
        if term < min_term:       # Once the terms surpass our precision stop
            break
    return e
"""
In my is_prime we check if the value is prime accounting for edge cases, like
1, 2 and if it's even. To narrow our pool we take the square root of the
prime we're testing and add 1 to account for rounding error. We then
modulo all odd values from 3 to the number's square root and if none 
result in 0 we have a prime number.
"""
def is_prime(n):
    if n < 2:
        return False              # Edge case ie. 1
    if n == 2:
        return True               # Edge case is prime ie. 2
    if n % 2 == 0:
        return False              # Edge case is even
    
    max_root = int(n ** .5) + 1   # Take the root of n and add 1 to account for int rounding
   
    # Check odd numbers up to the square root of that number
    for i in range(3, max_root, 2):
        if n % i == 0:            # Not prime if this is 0
            return False;
    return True;
"""
find_10_digit_prime first sets unacceptable terms to narrow our search and 
increase the efficiency of the program. We then start at the 3rd terms past 
the '2.' as at this point we've converted it to a string and cannot include 
that. We then account for our out of bounds by subracting 9 so we jump out
before the value would be NULL. We store 10 digits into our array to check.
We then cover the edge case that it is 10 digits due to a number being able 
to start with a 0. We then check if the number passes the is_prime test
if it does we've succesfully found our prime.
"""
def find_10_digit_prime(e_value_string):
    primes = []
    last_terms = [2,4,6,8,0,5]              # Unacceptable ending terms for 10 digit prime
    e_str = e_value_string[2:]              # Start at the 2nd element of the string to account for '2.'

    # Subtract 9 to account for out of bounds values once we approach the end of our precision
    for i in range(len(e_str) - 9):
        num = int(e_str[i:i+10])            # Get 10 digits from current i
        if len(str(num)) == 10:             # Check if the number is 10 digits
            if(num % 10 not in last_terms): # Check that the last digit is not one of our unacceptable terms
                if is_prime(num):           # Check if it passes prime test
                    primes.append(num)      # Add number to primes array
                    break
    return primes
"""
My code starts by importing decimal and getcontext, this will allow me to set a precison
level that I need that way I'm not going infinitly. Once prime_found is set to true
the program is breaks, we print the array and the condition of the while loop is 
broken.
"""
def main():

    precision = 100                 # Starting decimal precision
    max_precision = 1000            # Max decimal precision
    prime_found = False             

    while not prime_found and precision <= max_precision:
        
        getcontext().prec = precision               # Set precision
        e_value = calculate_e_log(precision)        # Get e value   
        e_value_string = str(e_value)               # Convert e to a string

        ten_digit_primes = find_10_digit_prime(e_value_string)  # Get 10 digit prime

        if ten_digit_primes:                        

            print(ten_digit_primes[0])              # Print 10 digit prime array
            prime_found = True                      # Enable our break clause
        else:
            precision += 100                        # Increase precision if not found

if __name__ == "__main__":
    main()
