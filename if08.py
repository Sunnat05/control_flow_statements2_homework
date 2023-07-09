def main(number):
    if number%7==1:
        return "Monday"
    elif number%7==2:
        return "Tuesday"
    elif number%7==3:
        return "Wednesday"
    elif number%7==4:
        return "Thursday"
    elif number%7==5:
        return "Friday"
    elif number%7==6:
        return "Saturday"
    elif number%7==0:
        return "Sunday"
print(main(34))
"""
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """