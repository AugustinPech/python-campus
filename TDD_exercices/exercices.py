def fizz_buzz(n):
    s=""
    if n % 3 == 0:
        s += "Fizz"
    if n % 5 == 0:
        s += "Buzz"
    if s == "":
        s = str(n)
    return s

def leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    if year % 4 == 0:
        return True
    else : 
        return False

def diamond_line(i, index, letters):
    diamond = ""
    if i==0 :
        diamond += " " * index + letters[i]
    else :
        diamond += " " * (index - i) + letters[i] + " " * (2*i-1) +  letters[i]
    return diamond

def diamond(letter) :
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = letters.index(letter)
    diamond = ""
    if index == 0 :
        return "A"
# forth
    for i in range(index + 1) :
        diamond += diamond_line(i, index, letters)
        diamond+= "\n"
# back
    for i in range(index -1, -1,-1) :
        diamond += diamond_line(i, index, letters)
        if i!=0 :
            diamond+= "\n"

    return diamond
