from math import sqrt
from math import ceil


def get_perfect_squares(start: int, end: int) -> list[int]:
    """Returneaza o lista cu patratele perfecte cuprinse intre o limita inferioara si o limita superioara date

    Args:
        start (int): limita inferioara
        end (int): limita superioara

    Returns:
        list[int]: Lista cu patratele perfect
    """
    squares = []

    square = ceil(sqrt(start))

    while True:
        if square**2 <= end:
            squares.append(square**2)
        else:
            break

        square += 1

    return squares


def test_get_perfect_squares():
    """Verifica get_perfect_squares
    """
    assert get_perfect_squares(9, 49) == [9, 16, 25, 36, 49]
    assert get_perfect_squares(20, 25) == [25]
    assert get_perfect_squares(10, 11) == []
    assert get_perfect_squares(300, 400) == [324, 361, 400]

test_get_perfect_squares()

def input_get_perfect_squares():
    print("Functia returneaza o lista cu patratele perfecte cuprinse intre o limita inferioara si o limita superioara date.")
    x = int(input("Limita inferioara = "))
    y = int(input("Limita superioara = "))
    print(f"Intre {x} si {y} exista urmatoarele patrate perfecte: {get_perfect_squares(x,y)}.")