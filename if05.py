def main(n):
    a=n//10000
    b=n//1000%10
    c=n//100%10
    d=n//10%10
    e=n%10
    if a>=b and a>=c and a>=d and a>=e:
        return a
    elif b>=a and b>=c and b>=d and b>=e:
        return b
    elif c>=a and c>=b and c>=d and c>=e:
        return c
    elif d>=a and d>=b and d>=c and d>=e:
        return d
    elif e>=a and e>=b and e>=c and e>=d:
        return e
print(main(57537))
"""
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """