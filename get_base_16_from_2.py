
def get_base_16_from_2(n: str) -> str:
    """Convertesete un numar din baza 2 in baza 16

    Args:
        n (str): [Numarul in baza 2 care va fi convertit]

    Returns:
        str: [Numarul in baza 16 dupa conversie]
    """

    if n == '0':
        return n

    # conversie din baza 2 in baza 10
    num = 0
    for i in range(len(n)):
        num += int(n[len(n)-i-1]) * (2 ** i)

    # conversie din baza 10 in baza 16
    new_n = ""
    base = 16
    digits = '0123456789ABCDEF'
    while num:
        new_n += digits[num % base]
        num //= 16

    return new_n[::-1]

    
def test_get_base_16_from_2():
    """Testeaza functia get_base_16_from_2
    """
    assert get_base_16_from_2("101") == '5'
    assert get_base_16_from_2("0") == '0'
    assert get_base_16_from_2("1") == '1'
    assert get_base_16_from_2("0101011") == '2B'
    

def input_get_base_16_from_2():
    x = input("Functia converteste un numar din baza 2 in baza 16. Ce numar sa fie convertit? ")
    print(f"Numarul in baza 2: {x}, convertit in baza 16, este: {get_base_16_from_2(x)}.")