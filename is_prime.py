def is_prime(n: int) -> bool:
    """Verifica daca un numar este prim

    Args:
        n (int): Numarul verificat

    Returns:
        bool: Daca este sau nu prim
    """
    if n < 2:
        return False
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True

def test_is_prime():
    """Testeaza is_prime
    """
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(29) == True

test_is_prime()