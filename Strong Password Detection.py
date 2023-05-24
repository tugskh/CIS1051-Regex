#Tugsbileg Khaliunbat
#CIS 1051
import re

def strongPassword():
    password = input("Enter a password: ")
    eightCharRegex = re.compile(r"\w{8,}")
    lowerCaseRegex = re.compile(r"[a-z]")
    upperCaseRegex = re.compile(r"[A-Z]")
    digitRegex = re.compile(r"\d+")
    if eightCharRegex.search(password) is not None:
        if lowerCaseRegex.search(password) is not None:
            if upperCaseRegex.search(password) is not None:
                if digitRegex.search(password) is not None:
                    print("Password is strong")
                else:
                    print("There is no digit.")
            else:
                print("There is no uppercase character.")
        else:
            print("There is no lowercase character.")
    else:
        print("Password should be at least eight characters long.")

strongPassword()
