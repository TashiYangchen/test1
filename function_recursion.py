def sum_of_digits(n):
    if n<10: # BAse case if n is a single-digit number, rerturn n
        return n
    else: # Recurssive case: calculate the sum of digit
        last_digit = n%10 # Get the last digit of n
        remaining_digits = n // 10 # Get the remaining digits by integer division with 10
        return last_digit + sum_of_digits(remaining_digits) # Recursively call the function with the remaining digits
                                                            # and add the last digit to the result 
print (sum_of_digits(123))