def get_leap_years(start: int, end: int) -> list[int]:
    """Returneaza anii bisecti intre doi ani dati

    Args:
        start (int): Primul an dat
        end (int): Al doilea an dat

    Returns:
        list[int]: O lista cu anii bisecti
    """
    leap_years = []

    for year in range(start, end+1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_years.append(year)

    return leap_years

def cooler_get_leap_years(start: int, end: int) -> list[int]:
    """Exact ca si get_leap_years, dar in 2 linii
    """
    from calendar import isleap
    return [year for year in range(start,end+1) if isleap(year)]

def test_get_leap_years():
    """Testeaza functia get_leap_years
    """
    assert get_leap_years(1888, 1920) == [1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920]
    assert get_leap_years(1910, 1950) == [1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948]
    assert get_leap_years(1981, 2052) == [1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052]
    assert get_leap_years(1,10) == [4, 8]

test_get_leap_years()