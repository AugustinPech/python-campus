while True:
    try :
        name = str(input ("what is your name ?"))
    except ValueError:
        print ("Please enter a valid name")
    else:
        break
        
print ("hello", name)

user_colors = input("Enter the three secondary colors separated by commas: ")
colors = [s.strip() for s in user_colors.split(",")]

print(f"List of colors: {colors}")