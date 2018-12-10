def test(number, odd=True):
    if odd == True:
        if (number % 2) == 1:
            return True
        else:
            return False
    else:
        if (number % 2) == 0:
            return True
        else:
            return False
