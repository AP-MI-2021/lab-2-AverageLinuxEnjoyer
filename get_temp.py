
def get_temp(temp: float, fromm: str, to: str) -> float:
    """Converteste o temperatura dintr-o scara data intr-o alta scara data

    Args:
        temp (float): Temperatura ce va fi convertita ('K'/'F'/'C')
        fromm (str): Scara in care se afla temperatura ('K'/'F'/'C')
        to (str): Scara in care se face conversia

    Returns:
        float: Noua temperatura in scara data
    """
    if fromm == 'C' and to == 'F':
        return (temp*9/5)+32
    elif fromm == 'C' and to == 'K':
        return temp+273
    elif fromm == 'F' and to == 'C':
        return 5/9 * (temp - 32)
    elif fromm == 'F' and to == 'K':
        return 5/9*(temp-32)+273
    elif fromm == 'K' and to == 'C':
        return temp - 273
    elif fromm == 'K' and to == 'F':
        return 9/5 * (temp-273) + 32


def test_get_temp():
    """Testeaza functia get_temp
    """
    assert get_temp(140, 'F', 'C') == 60.0
    assert get_temp(-18, 'C', 'F') == -0.3999999999999986
    assert get_temp(273, 'K', 'C') == 0
    assert get_temp(4, 'K', 'F') == -452.2
    assert get_temp(5503, 'C', 'K') == 5776
    assert get_temp(49,'C','F') == 120.2

test_get_temp()

def input_get_temp():
    print("Functia converteste o temperatura dintr-o scara data intr-o alta scara data.")
    temp = float(input("Temperatura = "))
    fromm = input("Scara temperaturii = ")
    to = input("Scara dorita = ")
    print(f"{temp} {fromm} = {get_temp(temp,fromm,to)} {to}")