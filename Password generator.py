import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

def pw_generator1():
    temp = ""
    while True:
        while True:
            length1 = input("length of password: ")
            if length1.isdigit() == False or length1 == "0":
                print("invalid input, please enter an integer!")
                continue
            else:
                break   
        while True:
            q1 = input("include digit?(yes/no) ").lower()
            if q1 == "yes":
                temp += digits
                break
            elif q1 == "no":
                break
            else:
                print("invalid input")
                continue
        while True:
            q2 = input("include symbols?(yes/no) ").lower()
            if q2 == "yes":
                temp += symbols
                break
            elif q2 == "no":
                break
            else:
                print("invalid input")
                continue
        while True:
            q3 = input("include Uppercase letters?(yes/no) ").lower()
            if q3 == "yes":
                temp += upper
                break
            elif q3 == "no":
                break
            else:
                print("invalid input")
                continue
        while True:
            q4 = input("include lowercase letter?(yes/no) ").lower()
            if q4 == "yes":
                temp += lower
                break
            elif q4 == "no":
                break
            else:
                print("invalid input")
                continue
        if q1 =="no" and q2 =="no" and q3 =="no" and q4 =="no":
            print("you should include at least one type of string!")
            continue
        
        pw1 = random.choices(temp, k = int(length1))
        password = "".join(pw1)
        print(password)
        go()
        
   
def pw_generator2():
    while True:
        while True:
            q1 = input("Enter the number of uppercase letter:")
            if q1.isdigit() == False:
                print("invalid input")
                continue
            else:
                break
        while True:
            q2 = input("Enter the number of lowercase letter:")
            if q2.isdigit() == False:
                print("invalid input")
                continue
            else:
                break
        while True:
            q3 = input("Enter the number of digit:")
            if q3.isdigit() == False:
                print("invalid input")
                continue
            else:
                break
        while True:
            q4 = input("Enter the number of symbols:")
            if q4.isdigit() == False:
                print("invalid input")
                continue
            else:
                break
            
        pw = random.choices(lower, k=int(q2)) + random.choices(upper, k=int(q1)) + random.choices(symbols, k=int(q4)) + random.choices(digits,k=int(q3))
        random.shuffle(pw)
        pwd = "".join(pw)
        print("Passowrd is", pwd)
        go()
        
def go():
    while True:
            back_to = input("continue?(yes/no")
            if back_to == "yes":
                initial()
            elif back_to == "no":
                print("thanks for using this application!Goodbye!")
                quit()
            else:
                print("invalid input")
     

def initial():
    while True:
        print("mode 1: allow you to choose the length of the password or whether include symbols, digits, uppercase letters or not.")
        print("mode 2: Allow you to enter the expected number of digits, symbols, uppercase and lowercase")
        choice = input("Which password generator do you want to use?(mode1/mode2): ").lower()
        if choice == "mode1":
            pw_generator1()
        elif choice == "mode2":
            pw_generator2()
        else:
            print("invalid input")
            continue
if __name__ = '__main__'
    initial()
