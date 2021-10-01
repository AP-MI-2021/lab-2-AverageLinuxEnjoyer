
def get_base_2(n: str) -> str:
    """Converteste un numar din baza 10 in baza 2

    Args:
        n (str): [Numarul in baza 10 inainte de conversie]

    Returns:
        str: [Numarul convertit in baza 2]
    """
    if n == 0:
        return "0"

    n = int(n)
    base = 2

    new_n = ""
    while n:
        new_n+=str(n%base)
        n//=base

    return new_n[::-1]

def test_get_base_2():
    """Verifica functia get_base_2
    """
    assert get_base_2(5) == "101"
    assert get_base_2(64) == "1000000"
    assert get_base_2(28) == "11100"
    assert get_base_2(1) == "1"
    assert get_base_2(0) == "0"
    assert get_base_2(482) == "111100010"
    assert get_base_2(237) == "11101101"

test_get_base_2()
