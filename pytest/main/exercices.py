def fizz_buzz(n):
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    if year % 4 == 0:
        return True
    else : 
        return False

def diamond(letter) :
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = letters.index(letter)
    diamond = ""
    if index == 0 :
        return "A"
# forth
    for i in range(index + 1) :
        if i==0 :
            diamond += " " * (index - i) + letters[i]
        else :
            diamond += " " * (index - i) + letters[i] + " " * (2*i-1) +  letters[i]
        diamond+= "\n"
# back
    for i in range(index -1, -1,-1) :
        if i==-1 :
            diamond += " " * (index - i) + letters[i]
        elif i==0 :
            diamond += " " * (index - i) + letters[i] 
        else :
            diamond += " " * (index - i) + letters[i] + " " * (2*i-1)+ letters[i] +"\n"

    return diamond
    