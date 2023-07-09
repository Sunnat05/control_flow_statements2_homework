def main(a,b,c):
    if b<=a<=c or c<=a<=b:
        return a
    elif a<=b<=c or c<=b<=a:
        return b
    elif a<=c<=b or b<=c<=a:
        return c
print(main(4,8,0))
"""    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """