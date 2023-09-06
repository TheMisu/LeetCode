def is_palindrome(x: int) -> bool:
    xStr = str(x)

    isPalin = True
    for i in range(len(xStr)):
        if xStr[i] != xStr[(len(xStr) - 1) - i]:
            isPalin = False
    
    return isPalin

print(is_palindrome(121))
print(is_palindrome(-121))