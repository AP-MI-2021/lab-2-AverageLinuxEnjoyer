from get_age_in_days import input_get_age_in_days
from get_base_2 import input_get_base_2
from get_base_16_from_2 import input_get_base_16_from_2
from get_cmmmc import input_get_cmmmc
from get_goldbach import input_get_goldbach
from get_largest_prime_below import input_get_largest_prime_below
from get_leap_years import input_get_leap_years
from get_n_choose_k import input_get_n_choose_k
from get_newton_sqrt import input_get_newton_sqrt
from get_perfect_squares import input_get_perfect_squares
from get_temp import input_get_temp
from is_antipalindrome import input_is_antipalindrome
from is_palindrome import input_is_palindrome
from is_superprime import input_is_superprime

def main():

    option = '?'
    while True:
        print("""
        Ce functie vrei sa foloesti?
        (1)    get_largest_prime_below
        (2)    get_age_in_days
        (3)    get_goldbach
        (4)    get_newton_sqrt
        (5)    is_palindrome
        (6)    is_superprim
        (7)    is_antipalindrom
        (8)    get_base_2
        (9)    get_base_16_from_2
        (10)   get_n_choose_k
        (11)   get_leap_years
        (12)   get_perfect_square
        (13)   get_temp
        (14)   get_cmmmc
        (X)    exit""", sep='')

        option = input("Optiune: ")
        
        if option == '1':
            input_get_largest_prime_below()
        elif option == '2':
            input_get_age_in_days()
        elif option == '3':
            input_get_goldbach()
        elif option == '4':
            input_get_newton_sqrt()
        elif option == '5':
            input_is_palindrome()
        elif option == '6':
            input_is_superprime()
        elif option == '7':
            input_is_antipalindrome()
        elif option == '8':
            input_get_base_2()
        elif option == '9':
            input_get_base_16_from_2()
        elif option == '10':
            input_get_n_choose_k()
        elif option == '11':
            input_get_leap_years()
        elif option == '12':
            input_get_perfect_squares()
        elif option == '13':
            input_get_temp()
        elif option == '14':
            input_get_cmmmc()
        else:
            break


if __name__ == "__main__":
    main()
