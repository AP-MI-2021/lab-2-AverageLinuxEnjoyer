import datetime

def get_age_in_days(birthday: str) -> int:
    """Determina varsta unei persoane in zile

    Args:
        birthday (str): Data nasterii

    Returns:
        int: Varsta in zile
    """
    date = datetime.date(int(birthday[6:]), int(birthday[3:5]), int(birthday[0:2]))
    today = datetime.date.today()
    
    difference = today - date
    return difference.days

def test_get_age_in_days():
    """n-am ce test sa fac, rezultatele se schimba zilnic
    """
    pass

def input_get_age_in_days():
    x = input("Functia va calcula varsta unei persoane exprimata in zile. Care este data nasterii? (format DD/MM/YYYY)")
    print(f"Varsta persoanei in este de {get_age_in_days(x)} zile.")