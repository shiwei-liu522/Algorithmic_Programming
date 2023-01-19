# Largest Concatenate Problem
# Compile the largest number by concatenating the given numbers.
# Input: A sequence of positive integers.
# Output: The largest number that can be obtained by concatenating the given integers in some order.

num = int(input())
digits = list(map(int, input().split()))
# digits = sorted(digits, reverse=True)

def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))

def largest_concatenate(digits):
    result = ""
    while digits:   # while digits is not empty
        max_digit = 0
        for digit in digits:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        result += str(max_digit)
        digits.remove(max_digit)
    return result

print(largest_concatenate(digits))
