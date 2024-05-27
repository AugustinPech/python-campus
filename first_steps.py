import os
import getpass
import pyinputplus as pyip


# ints and strings
for i in range(5):
    a=str(i)
    if i % 2 ==0 :
        a+=" is even"
    print(a)
# lists
a= list (range(5))
print (a)
print(type (a))
# tuples
def test():
    return 1,2,3
a= test()
print(a)
print(type(a))
a,b,c = test()
print(a)
print(b)
print(c)
print(type(a))
# dictionnaries
a = {'a':1,'b':2}
print(a)
print(type(a))
print(a['a'])
print(a['b'])
a['c']=3
print(a['c'])
for i in a.items():
    print(i)
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for key, value in a.items():
    print("" , key," = ",value)
# input   
# # input is always an integer
# while True:
#     try :
#         age = int(input ("what is your age ?"))
#     except ValueError:
#         print ("Please enter a valid age")
#     else:
#         break
        
# print ("your age is", age)

# # multiple inputs
# user_colors = input("Enter the three secondary colors separated by commas: ")
# colors = [s.strip() for s in user_colors.split(",")]

# print(f"List of colors: {colors}")


# # multiple input with checks

# questions = {
#     "What are the four colors of the Kenyan flag? ": {
#         "green", "black", "red", "white"
#     },
#     "What are the three colors of the French flag? ": {
#         "blue", "red", "white"
#     },
#     "How do you spell the first three numbers in Norwegian? ": {
#         "en", "to", "tre"
#     },
# }

# for question, correct in questions.items():
#     while True:
#         answers = {
#             answer.strip().lower() for answer in input(question).split(",")
#         }
#         if len(answers) == len(correct):
#             break
#         print(f"Please enter {len(correct)} answers separated by comma")
#     if answers == correct:
#         print("Correct")
#     else:
#         print(f"No, the correct answer is {', '.join(correct)}")

# # check e-mail

# def verify_email(email):
#     allowed_emails = [
#         email.strip() for email in os.getenv("ALLOWED_EMAILS").split(",")
#     ]
#     return email in allowed_emails

# def main():
#     email = getpass.getpass("Enter your email address: ")
#     if verify_email(email):
#         print("Email is valid. You can proceed.")
#     else:
#         print("Incorrect email. Access denied.")

# if __name__ == "__main__":
#     main()
    
# automating checks with pyinputplus
account_balance = 1000

print("Welcome to REALBank.")
while True:
    print(f"\nYour account balance: ${account_balance}")
    transaction_type = pyip.inputChoice(["Deposit", "Withdraw", "Exit"])

    if transaction_type == "Exit":
        break
    elif transaction_type == "Deposit":
        deposit_amount = pyip.inputInt(
            prompt="Enter amount (max $10,000): $", min=0, max=10000
        )
        account_balance += deposit_amount
        print(f"Deposited ${deposit_amount}.")
    elif transaction_type == "Withdraw":
        withdrawal_amount = pyip.inputInt(
            prompt="Enter amount: $", min=0, max=account_balance
        )
        account_balance -= withdrawal_amount
        print(f"Withdrew ${withdrawal_amount}.")

print("\nThank you for choosing REALBank. We hope to see you again soon!")