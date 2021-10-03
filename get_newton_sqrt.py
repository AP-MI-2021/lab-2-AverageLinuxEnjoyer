
def get_newton_sqrt(n: int, steps: int) -> float:
    """Gaseste o aproximare a radacinii patrate a unui numar dat, repetand de un numar de ori metoda lui Newton

    Args:
        n (int): Numarul a carei radacina trebuie gasita
        steps (int): Numarul de repetari a aplicarii metodei lui Newton

    Returns:
        float: Radacina aproximata
    """
    x = 2
    
    newtons_method = lambda nr: 0.5 * (x + n/x)

    for i in range(steps):
        x = newtons_method(n)

    return x

def test_get_newton_sqrt():
    """Testeaza get_newton_sqrt
    """
    assert get_newton_sqrt(36,4) == 6.00018310826276
    assert get_newton_sqrt(100,2) == 14.923076923076923
    assert get_newton_sqrt(16,7) == 4.0
    assert get_newton_sqrt(225,10) == 15.0 
    assert get_newton_sqrt(1,3) == 1.0003048780487804 

test_get_newton_sqrt()

def input_get_newton_sqrt():
    print("Functia calculeaza o aproximare a radacinii patrate a unui numar dat, repetand de un numar de ori metoda lui Newton.")
    x = int(input("La ce numar vrei sa-i gasesti radacina?"))
    y = int(input("De cate ori sa se repete metoda lui newton?"))

    print(f"Radacina patrata a lui {x} este {get_newton_sqrt(x,y)}")