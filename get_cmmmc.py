
def get_cmmmc_of_2(a: int, b: int) -> int:
    """Returnaza CMMMC a 2 numere

    Args:
        a (int): primul numar
        b (int): al doilea numar

    Returns:
        int: CMMMC a cele doua numere
    """
    if(a > b):
        num = a
        den = b
    else:
        num = b
        den = a
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    cmmdc = den
    cmmmc = int(int(a * b)/int(cmmdc))

    return cmmmc


def get_cmmmc(numbers: list[int]) -> int:
    """Returneaza CMMMC unei liste de numere

    Args:
        numbers (list[int]): Lista cu numerele

    Returns:
        int: CMMMC numerelor
    """
    if 0 in numbers:
        return 0

    cmmmc = get_cmmmc_of_2(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        cmmmc = get_cmmmc_of_2(cmmmc, numbers[i])

    return cmmmc


def test_get_cmmmc():
    """Testeaza get_cmmmc
    """
    assert get_cmmmc([36, 12, 48, 64]) == 576
    assert get_cmmmc([1,7,41,29]) == 8323
    assert get_cmmmc([1,2]) == 2
    assert get_cmmmc([23400, 5]) == 23400
    assert get_cmmmc([0, 486, 921]) == 0
    assert get_cmmmc([51,17,34,70]) == 3570

test_get_cmmmc()

