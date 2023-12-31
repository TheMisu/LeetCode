def is_palindrome(x: int) -> bool:
    xStr = str(x)

    isPalin = True
    for i in range(len(xStr)):
        if xStr[i] != xStr[(len(xStr) - 1) - i]:
            isPalin = False
    
    return isPalin

print(is_palindrome(121))
print(is_palindrome(-121))

def noString_palindrome(x: int) -> bool:
    # x cannot be a palindrome if it is a negative num or if it ends on 0
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    
    rev_num = 0
    
    # reversing x by adding its digits from last to first to rev_num
    while x > rev_num:
        rev_num = rev_num * 10 + x % 10 # this always adds x's last digit to rev_num
        x //= 10    # this ensures the next iteration starts from x's 2nd to last digit
    
    # if x.len is even then we have to check x == rev_num
    # else check x == rev_num // 10
    return x == rev_num or x == rev_num // 10

print(noString_palindrome(12321))