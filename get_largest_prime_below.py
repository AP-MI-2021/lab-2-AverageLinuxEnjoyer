from is_prime import is_prime

def get_largest_prime_below(n: int) -> int:
    """Returneaza cel mai mare numar prim sub o limita data

    Args:
        n (int): Limita superioara data

    Returns:
        int: Numarul prim returnat
    """
    for i in range(n-1, 0, -1):
        if is_prime(i):
            return i

def test_get_largest_prime_below():
    """Testeaza functia
    """
    assert get_largest_prime_below(30) == 29
    assert get_largest_prime_below(2498) == 2477
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(50) == 47

test_get_largest_prime_below()