def main(a,b):
    if a==b:
        return 0
    elif a>b:
        return a
    else:
        return b
print(main(9,9))
"""
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """