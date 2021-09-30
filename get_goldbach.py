from is_prime import is_prime
from get_largest_prime_below import get_largest_prime_below


def get_goldbach(n: int) -> (int, int):
    """[Returneaza o pereche cu cel mai mic, respectiv cel mai mare numar prim care insumate dau numarul oferit ca parametru]

    Args:
        n (int): [Intregul care va forma suma numerelor prime]

    Returns:
        (int,int): [Perechea de prime returnata]
    """
    if n % 2 == 1:
        return None

    primes = []
    x = n
    while True:
        x = get_largest_prime_below(x)

        if x == None:
            break

        primes.append(x)

    for a in reversed(primes):
        for b in primes:
            if a + b == n:
                return (a, b)


def test_get_goldbach():
    """[Testeaza get_goldbach]
    """
    assert get_goldbach(500) == (13, 487)
    assert get_goldbach(2) == None
    assert get_goldbach(3) == None
    assert get_goldbach(10) == (3, 7)
    assert get_goldbach(300) == (7, 293)
    assert get_goldbach(26) == (3, 23)
    assert get_goldbach(234) == (5, 229)









