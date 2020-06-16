"""Simple leapyear determination"""
def is_leapyear(year):
    """Rules : leap years are evenly divisible by four
    Century years are not leap years unless they are evenly divisible by 400
    """
    if year %4 == 0:
        if year % 400 == 0:
            return True
        if year %100 == 0:
            return False
        return True

    return False

if __name__ == "__main__":
    print("Is 2020 a leap year? {}".format(is_leapyear(2020)))