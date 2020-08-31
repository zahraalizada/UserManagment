#Welcome and control panel
print("""<<<<<<<<<<<<<< User data management system >>>>>>>>>>>>>>>

0. Enter 0 to exit the program
1. Enter Mode 1 to add a new user
2. Enter Mode 2 to delete user data according to User Id
3. Enter Mode 3 to change user information according to user ID.
4. Enter Mode 4 to display user information according to his/her name.
5. Enter Mode 5 to view all user data.
""")
# Adding user function
def addUser():
    userAdd = int(input("Enter the number of users you want to include: "))
    u = 0
    while u<userAdd:
        creatUser()
        userAdd-=1
#the end of the function

# A constructor that creates a user from user data
class User:
    def __init__(self, _id, _name, _surname, _age):
        self.id = _id
        self.name = _name
        self.surname = _surname
        self.age = _age

    def showUserData(self):
        print(
            f"İD: {self.id} / Ad: {self.name} / Soyad: {self.surname} / Yaş:{self.age}")

# A launched database to collect generated users
userDataStore = []

# Retrieval function of user information
def creatUser():
    idnum = input("Enter your ID number: ")
    while True:
        if (len(idnum)==3 and idnum.isdigit()):
            break
        else:
            idnum = input("Enter your ID number correctly: ")
    fname = input("Enter your name: ")
    while True:
        if fname.isalpha():
            break
        else:
            fname = input("Enter your name correctly: ")
    lname = input("Enter your surname: ")
    while True:
        if lname.isalpha():
            break
        else:
            lname = input("Enter your surname correctly: ")
    uage = input("Enter your age: ")
    while True:
        if (len(uage)==2 and uage.isdigit()):
            break
        else:
            uage = input("Enter your age correctly: ")
    userDataStore.append(User(idnum, fname, lname, uage))
#the end of the function

# A function to display data in the entire database
def showAllUsers():
    for u in userDataStore:
        u.showUserData()
#the end of the function

# The function to delete user data based on user ID
def deleteUserData():
    deleteNum = input("Enter the ID number of the user you want to delete: ")
    for dn in range(len(userDataStore)):
        if userDataStore[dn].id == deleteNum:
            userDataStore.pop(dn)
            break
#the end of the function

# A function to change the user  information according to the user ID
def modifyUserData():
    modifyNum = input("Enter the ID number of the user whose information you want to change: ")
    for mn in range(len(userDataStore)):
        if userDataStore[mn].id == modifyNum:
            newName = input("Enter a new name ")
            while True:
                if newName.isalpha():
                    break
                else:
                    newName = input("Enter your name correctly: ")
            newSurname = input("Enter a new surname: ")
            while True:
                if newSurname.isalpha():
                    break
                else:
                    newSurname = input("Enter your surname correctly:")
            newAge = input("Enter the new age: ")
            while True:
                if (len(newAge)==2 and newAge.isdigit()):
                    break
                else:
                    newAge = input("Enter your age correctly: ")

            userDataStore[mn].name = newName
            userDataStore[mn].surname = newSurname
            userDataStore[mn].age = newAge
            userDataStore[mn].showUserData()
#the end of the function

# Finding user information according to the username
def nameShowData():
    nameData = input("Enter the name of the user whose information you want to find: ")
    for nd in range(len(userDataStore)):
        if userDataStore[nd].name == nameData:
            userDataStore[nd].showUserData()
#the end of the function

# Control panel
while True:
    operation = input("Select the appropriate operation: ")
    if operation == "0":
        print("Thank you for using the program!")
        break
    elif operation == "1":
        addUser()
        print("User information has been entered!")
    elif (operation == "2" and len(userDataStore)!=0):
        deleteUserData()
        print("User information has been deleted!")
    elif (operation == "3" and len(userDataStore)!=0):
        modifyUserData()
        print("User information has been changed!")
    elif (operation == "4" and len(userDataStore)!=0):
        nameShowData()
    elif (operation == "5" and len(userDataStore)!=0):
        showAllUsers()
    else:
        print("Enter the correct mode ")
