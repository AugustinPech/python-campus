import main.exercices as ex

def test_fizz_buzz() :
    for i in range(1, 100) :
        if i % 3 == 0 :
            assert ex.fizz_buzz(i) == "Fizz"
        elif i % 5 == 0 :
            assert ex.fizz_buzz(i) == "Buzz"
        else :
            assert ex.fizz_buzz(i) == str(i)
def test_leap_years():
    assert ex.leap_year(2000) == True
    assert ex.leap_year(2001) == False
    assert ex.leap_year(1700) == False
    assert ex.leap_year(1800) == False
    assert ex.leap_year(1900) == False
    assert ex.leap_year(2100) == False
    assert ex.leap_year(2200) == False
    assert ex.leap_year(2008) == True
    assert ex.leap_year(2012) == True
    assert ex.leap_year(2016) == True
    assert ex.leap_year(2020) == True
    assert ex.leap_year(2017) == False
    assert ex.leap_year(2018) == False
    assert ex.leap_year(2019) == False

def test_diamond():
    assert ex.diamond("A") == "A"
    assert ex.diamond("B") == " A\nB B\n A"
    assert ex.diamond("C") == "  A\n B B\nC   C\n B B\n  A"
    assert ex.diamond("D") == "   A\n  B B\n C   C\nD     D\n C   C\n  B B\n   A"
    assert ex.diamond("E") == "    A\n   B B\n  C   C\n D     D\nE       E\n D     D\n  C   C\n   B B\n    A"
    