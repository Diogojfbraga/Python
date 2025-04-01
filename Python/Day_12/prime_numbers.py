def is_prime(num):
    """
    Determines if a number is prime.

    A prime number has exactly two positive divisors: 1 and itself.
    This function checks how many times 'num' is divisible by numbers from 1 to 'num'.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if 'num' is prime, False otherwise.
    """
    count = 0  # Counter for the number of divisors
    original_num = num  # Store original number for divisibility check

    # Check how many numbers divide evenly into 'original_num'
    while num > 0:
        if original_num % num == 0:
            count += 1
        num -= 1  # Decrement the divisor

    print(f"Total divisors for {original_num}: {count}")

    # A prime number has exactly two divisors: 1 and itself
    return count == 2

# Test with a prime number
print(is_prime(73))  
