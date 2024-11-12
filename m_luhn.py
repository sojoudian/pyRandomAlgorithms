def luhn_check(number):
    digits = [int(d) for d in str(number)]
    checksum = 0

    # Process every digit, starting from the right
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        # Double every second digit from the right
        if (len(digits) - i) % 2 == 0:
            digit *= 2
            # If doubling the digit results in a number greater than 9, subtract 9
            if digit > 9:
                digit -= 9
        # Add the processed digit to the checksum
        checksum += digit

    # If the checksum is divisible by 10, the number is valid
    return checksum % 10 == 0

# Example usage:
number = 79927398713
if luhn_check(number):
    print(f"{number} is valid.")
else:
    print(f"{number} is not valid.")

