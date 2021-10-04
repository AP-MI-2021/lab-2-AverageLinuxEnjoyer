# from get_age_in_days import input_get_age_in_days
# from get_base_2 import input_get_base_2
# from get_base_16_from_2 import input_get_base_16_from_2
# from get_cmmmc import input_get_cmmmc
# from get_goldbach import input_get_goldbach
# from get_largest_prime_below import input_get_largest_prime_below
# from get_leap_years import input_get_leap_years
# from get_n_choose_k import input_get_n_choose_k
# from get_newton_sqrt import input_get_newton_sqrt
# from get_perfect_squares import input_get_perfect_squares
# from get_temp import input_get_temp
# from is_antipalindrome import input_is_antipalindrome
# from is_palindrome import input_is_palindrome
# from is_superprime import input_is_superprime

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

def is_palindrome(n : int) -> bool:
    """Verifica daca numarul dat este un palindrom

    Args:
        n (int): Numarul care este verificat

    Returns:
        bool: Daca este sau nu palindrom
    """
    inverse = 0
    length = len(str(n))

    for i in range(length // 2):
        inverse*=10
        inverse+=n%10
        n//=10

    if length % 2 == 1:
        n//=10

    return n == inverse

def test_is_palidnrome():
    """Testeaza is_palindrome
    """
    assert is_palindrome(1234321) == True
    assert is_palindrome(52525) == True
    assert is_palindrome(1234) == False
    assert is_palindrome(5) == True
    assert is_palindrome(101) == True

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

def main():
    option = '?'
    while True:
        print("Ce functie vrei sa foloseti?")
        print("(1) get_largest_prime_below")
        print("(2) is_palindrome")
        print("(3) is_antipalindrom")
        print("(x) exit")

        option = input()

        if option == '1':
            x = int(input("Functia va gasi cel mai mare numar prim mai mic decat o limita superioara. Care este limita superioara? "))
            print(f"Cel mai mare numar prim mai mic decat {x} este {get_largest_prime_below(x)}.")
        elif option == '2':
            x = int(input("Functia verifica daca un numar este palindrom. Ce numar doresti sa verifici? "))
            if is_palindrome(x):
                print(x, "este palindrom.")
            else:
                print(x, "nu este palindrom.")
        elif option == '3':
            x = int(input("Verifica daca un numar este antipalindrom. Un numar este antipalindrom daca oricare dooua cifre egal departate de extremitati sunt diferite. Ce numar vrei sa verifici? "))
            if is_antipalindrome(x):
                print(x, "este antipalindrom.")
            else:
                print(x, "nu este antipalindrom.")
        else:
            break


    # option = '?'
    # while True:
    #     print("""
    #     Ce functie vrei sa foloesti?
    #     (1)    get_largest_prime_below
    #     (2)    get_age_in_days
    #     (3)    get_goldbach
    #     (4)    get_newton_sqrt
    #     (5)    is_palindrome
    #     (6)    is_superprim
    #     (7)    is_antipalindrom
    #     (8)    get_base_2
    #     (9)    get_base_16_from_2
    #     (10)   get_n_choose_k
    #     (11)   get_leap_years
    #     (12)   get_perfect_square
    #     (13)   get_temp
    #     (14)   get_cmmmc
    #     (X)    exit""", sep='')

    #     option = input("Optiune: ")
        
    #     if option == '1':
    #         input_get_largest_prime_below()
    #     elif option == '2':
    #         input_get_age_in_days()
    #     elif option == '3':
    #         input_get_goldbach()
    #     elif option == '4':
    #         input_get_newton_sqrt()
    #     elif option == '5':
    #         input_is_palindrome()
    #     elif option == '6':
    #         input_is_superprime()
    #     elif option == '7':
    #         input_is_antipalindrome()
    #     elif option == '8':
    #         input_get_base_2()
    #     elif option == '9':
    #         input_get_base_16_from_2()
    #     elif option == '10':
    #         input_get_n_choose_k()
    #     elif option == '11':
    #         input_get_leap_years()
    #     elif option == '12':
    #         input_get_perfect_squares()
    #     elif option == '13':
    #         input_get_temp()
    #     elif option == '14':
    #         input_get_cmmmc()
    #     else:
    #         break


if __name__ == "__main__":
    main()

