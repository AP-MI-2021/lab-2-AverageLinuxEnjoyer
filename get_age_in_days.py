import datetime

def get_age_in_days(birthday: str) -> int:
    """[Determina varsta unei persoane in zile]

    Args:
        birthday (str): [Data nasterii]

    Returns:
        int: [Varsta in zile]
    """
    date = datetime.date(int(birthday[6:]), int(birthday[3:5]), int(birthday[0:2]))
    today = datetime.date.today()
    
    difference = today - date
    return difference.days

def test_get_age_in_days():
    """[n-am ce test sa fac]
    """
    pass