from is_prime import is_prime

def is_superprime(n: int) -> bool:
    """Verifica daca numarul dat ca parametru si toate prefixele lui sunt prime

    Args:
        n (int): Numarul verificat

    Returns:
        bool: True daca toate numerele sunt prime, False in caz contrar
    """

    while n:
        if not is_prime(n):
            return False

        n //= 10

    return True

def test_is_superprime():
    """Testeaza is_superprime
    """
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(29) == True
    assert is_superprime(1) == False

test_is_superprime()

def input_is_superprime():
    x = int(input("Functia verifica daca un numar si toate prefixele sale sunt prime. Ce numar sa fie verificat? "))
    if is_superprime(x):
        print(x, "este superprim.")
    else:
        print(x, "nu este superprim.")