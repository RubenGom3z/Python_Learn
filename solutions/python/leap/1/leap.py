def leap_year(year):
    ayuda = int(year % 100)
    if ayuda == 0:
        resultado = int(year % 400)
        if resultado == 0:
            return True
        else:
            return False
    ayuda = int (year % 4)
    if ayuda == 0:
        return True
    else:
        return False
    pass
