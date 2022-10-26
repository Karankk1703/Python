import pandas
import csv
import re

fileName = "UserDetailsFile.csv"
def GetUserDetails():
    global userName
    global password
    userName = str(input("Enter Username: "))
    password = str(input("Enter Password: "))


def ValidateEmail():
    regex = r'\b[A-Za-z0-9._%+-@.]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, userName)):
        return True
    else:
        print("Invalid Email")
        return False

def CheckNumber():
    if(userName[0].isnumeric()):
        print("First character of the userName should not be a number")
        return False
    else:
        return True

def ValidatePassword():
    specialChar = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    res = any(chr.isupper() for chr in password)
    res = res and any(chr.islower() for chr in password)
    res = res and any(chr.isnumeric() for chr in password)
    res = res and specialChar.search(password)
    return res

def CheckForDotAfterAt():
    userNameSplitList = userName.split('@')
    ListLength = len(userNameSplitList)
    if(ListLength>0):
        if(userNameSplitList[ListLength-1][0] != '.'):
            return True
        else:
            return False
    else:
        return False

def register():
    isValidEmail = False
    isValidaPass = False
    GetUserDetails()
    if(ValidateEmail()):
        isValidEmail = CheckNumber()
        isValidEmail = isValidEmail and CheckForDotAfterAt()
    else:
        print("Enter valid Email Id")
    passwordLenght = len(password)
    if(passwordLenght>5 and passwordLenght < 16):
        if(ValidatePassword()):
            print("Password accepted")
            isValidaPass = True
        else:
            print("password does not match the criteria")
    else:
        isValidaPass = False
        print("password should have more then 5 character and less then 16")

    if(isValidaPass and isValidEmail):
        if(not CheckForUserExist()):
            WriteCSV()
        else:
            print(userName,"Already exists")


def WriteCSV():
    row = [userName,password]
    with open(fileName,'a', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(row)
        csvfile.close()
def ReadCSV():
    with open(fileName, 'r') as csvfile:
        csvRead = csv.reader(csvfile)
        res = list(csvRead)
        print(res)
        return res
def CheckForUserExist():
    csvRead = ReadCSV()
    for row in csvRead:
        if(row[0] == userName):
            return True

    return False

def CheckForPasswordExist():
    csvRead = ReadCSV()
    for row in csvRead:
        if(row[1] == password):
            return True

    return False

def GetNewPassword():
    username = str(input("Enter Username: "))
    password1 = str(input("Enter password: "))
    confirmPassword = str(input("Enter Confirm password: "))
    lines = list()
    if(password1 == confirmPassword):
        csvContent = ReadCSV()
        print(csvContent)
        for row in csvContent:
            print(row)
            lines.append(row)
            print(row[0])
            if (row[0] == username):
                lines.remove(row)
                row[1] = password1
                lines.append(row)
                print("row",row)
        print("line",lines)
        with open(fileName, 'w', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            for element in lines:
                row = [element[0], element[1]]
                print(row)
                csvWriter.writerow(row)
    else:
        print("Password mismatch")
def ForgetPassword():
    retrievePass = input("Do you want to retrieve password [y/n]:")
    userName=""
    if(retrievePass.lower() =='y'):
        userName = str(input("Enter Username: "))
        csvContent = ReadCSV()
        for row in csvContent:
            if(row[0] == userName):
                print(row[1])
    else:
        GetNewPassword()



def loginfunction():
    GetUserDetails()
    if(not CheckForUserExist()):
        print("user name not exist. Please register!")
        register()
    else:
        if(CheckForPasswordExist()):
            print("Login Success")
        else:
            print("User name or password is invalid")
            forgetPassordOption = input("Forget password [y/n]: ")
            if(forgetPassordOption.lower() == 'y'):
                ForgetPassword()



signOption = int(input("1. Login\n2. Register\n3. Forgot password\nSelect option : "))
if (signOption == 1):
    loginfunction()
elif (signOption ==2):
    register()
elif (signOption==3):
    ForgetPassword()
else:
    ReadCSV()
    print("Select correct option")