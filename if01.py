def main(a,b,c):
    if a>b and a>c:
        return "First number"
    elif b>a and b>c:
        return "Second number"
    elif c>a and c>b:
        return "Third number"
print(main(9,7,10))
"""
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """