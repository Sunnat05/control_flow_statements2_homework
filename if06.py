def main(n):
     a=n//10000
     b=n//1000%10
     c=n//100%10
     d=n//10%10
     e=n%10
     if a>=b and a>=c and a>=d and a>=e:
        return a**2
     elif b>=a and b>=c and b>=d and b>=e:
        return b**2
     elif c>=a and c>=b and c>=d and c>=e:
        return c**2
     elif d>=a and d>=b and d>=c and d>=e:
        return d**2
     elif e>=a and e>=b and e>=c and e>=d:
        return e**2
print(main(57537))
"""
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """