def reverse(x: int) -> int:
    """Returneaza un numar scris invers

    Args:
        x (int): Numarul care urmeaza a fi inversat

    Returns:
        int: Numarul inversat
    """
    y = 0
    while x:
        y *= 10
        y += x % 10
        x //= 10

    return y


def is_antipalindrome(n: int) -> bool:
    """Verifica daca un numar este antipalindrom. Un numar este antipalindrom daca oricare dooua cifre egal departate de extremitati sunt diferite.

    Args:
        n (int): Numarul verificat

    Returns:
        bool: Daca este sau nu antipalindrom
    """

    rev = reverse(n)
    for i in range(len(str(n)) // 2):
        if n%10==rev%10:
            return False

        n//=10
        rev//=10

    return True

def test_is_antipalindrome():
    """Verifica is_antipalindrome
    """
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False
    assert is_antipalindrome(19286452) == True
    assert is_antipalindrome(11) == False
    assert is_antipalindrome(1) == True

test_is_antipalindrome()

def input_is_antipalindrome():
    x = int(input("Verifica daca un numar este antipalindrom. Un numar este antipalindrom daca oricare dooua cifre egal departate de extremitati sunt diferite. Ce numar vrei sa verifici? "))
    if is_antipalindrome(x):
        print(x, "este antipalindrom.")
    else:
        print(x, "nu este antipalindrom.")
