def main(a,b,c):
    if b<a<c or c<a<b:
        return "First number"
    elif a<b<c or c<b<a:
        return "Second number"
    elif a<c<b or b<c<a:
        return "Third number"
print(main(4,8,0))
"""    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """