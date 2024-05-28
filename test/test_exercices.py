import TDD_exercices.exercices as ex
import pytest
@pytest.mark.parametrize("n", [
    3, 6, 9, 12,21,24,27,30,33
])
def test_fizz_buzz(n) :
    assert ex.fizz_buzz(n) == "Fizz"

@pytest.mark.parametrize("n", [
    5, 10, 20, 25, 35, 40, 50, 55, 65
])
def test_fizz_buzz(n) :
    assert ex.fizz_buzz(n) == "Buzz"

@pytest.mark.parametrize("n", [
    15, 30, 45, 60, 75, 90, 105, 120, 135
])
def test_fizz_buzz(n) :
    assert ex.fizz_buzz(n) == "FizzBuzz"

@pytest.mark.parametrize("n", [
    1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19
])
def test_fizz_buzz(n) :
    assert ex.fizz_buzz(n) == str(n)

@pytest.mark.parametrize("n", [
    2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040,2000, 2400, 2800, 3200, 3600
])
def test_leap_years(n):
    assert ex.leap_year(n) == True
    
@pytest.mark.parametrize("n", [
    2001, 2002, 2003, 2005, 2006, 2007, 2009, 2010, 2011, 2013, 2014, 2015, 2017, 2018, 2019
])
def test_leap_years(n):
    assert ex.leap_year(n) == False

@pytest.mark.parametrize("n", [
    1700, 1900, 2100
])
def test_leap_years(n):
    assert ex.leap_year(n) == False

@pytest.mark.parametrize("letter,expected", [
("A","A"),
("B"," A\nB B\n A"),
("C","  A\n B B\nC   C\n B B\n  A"),
("D","   A\n  B B\n C   C\nD     D\n C   C\n  B B\n   A"),
("E","    A\n   B B\n  C   C\n D     D\nE       E\n D     D\n  C   C\n   B B\n    A"),
("F","     A\n    B B\n   C   C\n  D     D\n E       E\nF         F\n E       E\n  D     D\n   C   C\n    B B\n     A"),
("G","      A\n     B B\n    C   C\n   D     D\n  E       E\n F         F\nG           G\n F         F\n  E       E\n   D     D\n    C   C\n     B B\n      A"),
("H","       A\n      B B\n     C   C\n    D     D\n   E       E\n  F         F\n G           G\nH             H\n G           G\n  F         F\n   E       E\n    D     D\n     C   C\n      B B\n       A"),
("I","        A\n       B B\n      C   C\n     D     D\n    E       E\n   F         F\n  G           G\n H             H\nI               I\n H             H\n  G           G\n   F         F\n    E       E\n     D     D\n      C   C\n       B B\n        A"),
("J","         A\n        B B\n       C   C\n      D     D\n     E       E\n    F         F\n   G           G\n  H             H\n I               I\nJ                 J\n I               I\n  H             H\n   G           G\n    F         F\n     E       E\n      D     D\n       C   C\n        B B\n         A"),
("K","          A\n         B B\n        C   C\n       D     D\n      E       E\n     F         F\n    G           G\n   H             H\n  I               I\n J                 J\nK                   K\n J                 J\n  I               I\n   H             H\n    G           G\n     F         F\n      E       E\n       D     D\n        C   C\n         B B\n          A"),
("L","           A\n          B B\n         C   C\n        D     D\n       E       E\n      F         F\n     G           G\n    H             H\n   I               I\n  J                 J\n K                   K\nL                     L\n K                   K\n  J                 J\n   I               I\n    H             H\n     G           G\n      F         F\n       E       E\n        D     D\n         C   C\n          B B\n           A"),
("M","            A\n           B B\n          C   C\n         D     D\n        E       E\n       F         F\n      G           G\n     H             H\n    I               I\n   J                 J\n  K                   K\n L                     L\nM                       M\n L                     L\n  K                   K\n   J                 J\n    I               I\n     H             H\n      G           G\n       F         F\n        E       E\n         D     D\n          C   C\n           B B\n            A"),
("N","             A\n            B B\n           C   C\n          D     D\n         E       E\n        F         F\n       G           G\n      H             H\n     I               I\n    J                 J\n   K                   K\n  L                     L\n M                       M\nN                         N\n M                       M\n  L                     L\n   K                   K\n    J                 J\n     I               I\n      H             H\n       G           G\n        F         F\n         E       E\n          D     D\n           C   C\n            B B\n             A"),
("O","              A\n             B B\n            C   C\n           D     D\n          E       E\n         F         F\n        G           G\n       H             H\n      I               I\n     J                 J\n    K                   K\n   L                     L\n  M                       M\n N                         N\nO                           O\n N                         N\n  M                       M\n   L                     L\n    K                   K\n     J                 J\n      I               I\n       H             H\n        G           G\n         F         F\n          E       E\n           D     D\n            C   C\n             B B\n              A"),
("P","               A\n              B B\n             C   C\n            D     D\n           E       E\n          F         F\n         G           G\n        H             H\n       I               I\n      J                 J\n     K                   K\n    L                     L\n   M                       M\n  N                         N\n O                           O\nP                             P\n O                           O\n  N                         N\n   M                       M\n    L                     L\n     K                   K\n      J                 J\n       I               I\n        H             H\n         G           G\n          F         F\n           E       E\n            D     D\n             C   C\n              B B\n               A"),
("Q","                A\n               B B\n              C   C\n             D     D\n            E       E\n           F         F\n          G           G\n         H             H\n        I               I\n       J                 J\n      K                   K\n     L                     L\n    M                       M\n   N                         N\n  O                           O\n P                             P\nQ                               Q\n P                             P\n  O                           O\n   N                         N\n    M                       M\n     L                     L\n      K                   K\n       J                 J\n        I               I\n         H             H\n          G           G\n           F         F\n            E       E\n             D     D\n              C   C\n               B B\n                A"),
("R","                 A\n                B B\n               C   C\n              D     D\n             E       E\n            F         F\n           G           G\n          H             H\n         I               I\n        J                 J\n       K                   K\n      L                     L\n     M                       M\n    N                         N\n   O                           O\n  P                             P\n Q                               Q\nR                                 R\n Q                               Q\n  P                             P\n   O                           O\n    N                         N\n     M                       M\n      L                     L\n       K                   K\n        J                 J\n         I               I\n          H             H\n           G           G\n            F         F\n             E       E\n              D     D\n               C   C\n                B B\n                 A"),
("S","                  A\n                 B B\n                C   C\n               D     D\n              E       E\n             F         F\n            G           G\n           H             H\n          I               I\n         J                 J\n        K                   K\n       L                     L\n      M                       M\n     N                         N\n    O                           O\n   P                             P\n  Q                               Q\n R                                 R\nS                                   S\n R                                 R\n  Q                               Q\n   P                             P\n    O                           O\n     N                         N\n      M                       M\n       L                     L\n        K                   K\n         J                 J\n          I               I\n           H             H\n            G           G\n             F         F\n              E       E\n               D     D\n                C   C\n                 B B\n                  A"),
("T","                   A\n                  B B\n                 C   C\n                D     D\n               E       E\n              F         F\n             G           G\n            H             H\n           I               I\n          J                 J\n         K                   K\n        L                     L\n       M                       M\n      N                         N\n     O                           O\n    P                             P\n   Q                               Q\n  R                                 R\n S                                   S\nT                                     T\n S                                   S\n  R                                 R\n   Q                               Q\n    P                             P\n     O                           O\n      N                         N\n       M                       M\n        L                     L\n         K                   K\n          J                 J\n           I               I\n            H             H\n             G           G\n              F         F\n               E       E\n                D     D\n                 C   C\n                  B B\n                   A"),
("U","                    A\n                   B B\n                  C   C\n                 D     D\n                E       E\n               F         F\n              G           G\n             H             H\n            I               I\n           J                 J\n          K                   K\n         L                     L\n        M                       M\n       N                         N\n      O                           O\n     P                             P\n    Q                               Q\n   R                                 R\n  S                                   S\n T                                     T\nU                                       U\n T                                     T\n  S                                   S\n   R                                 R\n    Q                               Q\n     P                             P\n      O                           O\n       N                         N\n        M                       M\n         L                     L\n          K                   K\n           J                 J\n            I               I\n             H             H\n              G           G\n               F         F\n                E       E\n                 D     D\n                  C   C\n                   B B\n                    A"),
("V","                     A\n                    B B\n                   C   C\n                  D     D\n                 E       E\n                F         F\n               G           G\n              H             H\n             I               I\n            J                 J\n           K                   K\n          L                     L\n         M                       M\n        N                         N\n       O                           O\n      P                             P\n     Q                               Q\n    R                                 R\n   S                                   S\n  T                                     T\n U                                       U\nV                                         V\n U                                       U\n  T                                     T\n   S                                   S\n    R                                 R\n     Q                               Q\n      P                             P\n       O                           O\n        N                         N\n         M                       M\n          L                     L\n           K                   K\n            J                 J\n             I               I\n              H             H\n               G           G\n                F         F\n                 E       E\n                  D     D\n                   C   C\n                    B B\n                     A"),
("W","                      A\n                     B B\n                    C   C\n                   D     D\n                  E       E\n                 F         F\n                G           G\n               H             H\n              I               I\n             J                 J\n            K                   K\n           L                     L\n          M                       M\n         N                         N\n        O                           O\n       P                             P\n      Q                               Q\n     R                                 R\n    S                                   S\n   T                                     T\n  U                                       U\n V                                         V\nW                                           W\n V                                         V\n  U                                       U\n   T                                     T\n    S                                   S\n     R                                 R\n      Q                               Q\n       P                             P\n        O                           O\n         N                         N\n          M                       M\n           L                     L\n            K                   K\n             J                 J\n              I               I\n               H             H\n                G           G\n                 F         F\n                  E       E\n                   D     D\n                    C   C\n                     B B\n                      A"),
("X","                       A\n                      B B\n                     C   C\n                    D     D\n                   E       E\n                  F         F\n                 G           G\n                H             H\n               I               I\n              J                 J\n             K                   K\n            L                     L\n           M                       M\n          N                         N\n         O                           O\n        P                             P\n       Q                               Q\n      R                                 R\n     S                                   S\n    T                                     T\n   U                                       U\n  V                                         V\n W                                           W\nX                                             X\n W                                           W\n  V                                         V\n   U                                       U\n    T                                     T\n     S                                   S\n      R                                 R\n       Q                               Q\n        P                             P\n         O                           O\n          N                         N\n           M                       M\n            L                     L\n             K                   K\n              J                 J\n               I               I\n                H             H\n                 G           G\n                  F         F\n                   E       E\n                    D     D\n                     C   C\n                      B B\n                       A"),
("Y","                        A\n                       B B\n                      C   C\n                     D     D\n                    E       E\n                   F         F\n                  G           G\n                 H             H\n                I               I\n               J                 J\n              K                   K\n             L                     L\n            M                       M\n           N                         N\n          O                           O\n         P                             P\n        Q                               Q\n       R                                 R\n      S                                   S\n     T                                     T\n    U                                       U\n   V                                         V\n  W                                           W\n X                                             X\nY                                               Y\n X                                             X\n  W                                           W\n   V                                         V\n    U                                       U\n     T                                     T\n      S                                   S\n       R                                 R\n        Q                               Q\n         P                             P\n          O                           O\n           N                         N\n            M                       M\n             L                     L\n              K                   K\n               J                 J\n                I               I\n                 H             H\n                  G           G\n                   F         F\n                    E       E\n                     D     D\n                      C   C\n                       B B\n                        A"),
("Z","                         A\n                        B B\n                       C   C\n                      D     D\n                     E       E\n                    F         F\n                   G           G\n                  H             H\n                 I               I\n                J                 J\n               K                   K\n              L                     L\n             M                       M\n            N                         N\n           O                           O\n          P                             P\n         Q                               Q\n        R                                 R\n       S                                   S\n      T                                     T\n     U                                       U\n    V                                         V\n   W                                           W\n  X                                             X\n Y                                               Y\nZ                                                 Z\n Y                                               Y\n  X                                             X\n   W                                           W\n    V                                         V\n     U                                       U\n      T                                     T\n       S                                   S\n        R                                 R\n         Q                               Q\n          P                             P\n           O                           O\n            N                         N\n             M                       M\n              L                     L\n               K                   K\n                J                 J\n                 I               I\n                  H             H\n                   G           G\n                    F         F\n                     E       E\n                      D     D\n                       C   C\n                        B B\n                         A")
])
def test_diamond(letter ,expected):
    assert ex.diamond(letter) == expected

