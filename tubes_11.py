# WELCOME TO TEMPDEC

# bagian 1 (login & register)

# Infinity loop (ga akan pernah selesai) 
# pros: program lebih detail (memudahkan user), bisa log in ke username yg udh diregister sblmmya/switch account (register dgn alamat email, no telp & username baru)
# cons: bikin flowchart & pseudocodenya ribet

from random import randint

#Bacanya dari paling bawah

logged=False
app = True
arr_name = ["empty"]
arr_email = ["empty"]
arr_phone = [0]
arr_password = ["empty"]
welcome = "Welcome to TempDec!"

def regis_email():
    loop =True
    global arr_email
    while loop:
        email = input("Please enter your email          : ")
        confirm=True
        for element in arr_email:
            if element == email:
                confirm = False
                print("This email address has already been registered into another account. Please choose another one.")
        if confirm:
            arr_email.append(email)
            loop = False
    return 
            
def regis_phone():
    loop =True
    global arr_phone
    while loop:
        phone = input("Please enter your phone number   : ")
        confirm=True
        for element in arr_phone:
            if element == phone:
                confirm = False
                print("This phone number has already been registered into another account. Please choose another one.")
        if confirm:
            arr_phone.append(phone)
            loop = False
    return 

def regis_username():
    loop = True
    global arr_name, arr_password
    while loop:
        username = input("Please enter your username     : ")
        confirm=True
        for element in arr_name:
            if element == username:
                confirm = False
                print("This username has already been taken. Please choose another one.")
        if confirm:
            arr_name.append(username)
            loop = False
    password = input("Please enter your password      : ")
    arr_password.append(password)
    return 

def regis_otp():
    arr_otp = []
    confirm=True
    loop=True
    while loop:
        otp = randint(100, 1000)
        loop = ("y" or "yes") in input("You received the code: " + str(otp) + ", do you want us to send another code? (y/n): ").lower()
        arr_otp.append(otp)
    loop=True
    while loop:
        code = int(input("Insert the code you have received: "))
        if code == arr_otp[len(arr_otp)-1]:
            memo = input("I accept the privacy and policy terms of this application (y/n): ")
            while confirm:
                if memo == "y" or "yes" or "oke" or "ok":
                    print("Congratulations! You have succesfully signed in to TempDec ^_^")
                    loop=False
                    confirm=False
                else:
                    print("You must agree to the privacy and policy terms of this application to continue using this app.")
        else:
            print("Please enter the latest code.")

#########################################################################################################################################
def regis_main(logged):
    reg = input("Please register in to use the application! (click ok to continue): ").lower()
    if reg == "ok":
        m = input("TempDec wants to ask for access to your location, files, and camera (click ok to continue): ").lower()
        if m == "ok":
            regis_email() 
            regis_phone()
            regis_username()
            regis_otp()
            logged=True
            return logged
#########################################################################################################################################
def login_main(logged):
    global arr_name, arr_password
    loop = True
    n = 5
    while loop:
        name = input("Please enter your username       :")
        password = input("Please enter your password    :")
        i=-1
        for e in arr_name:
            i+=1
            if name == e:
                if password == arr_password[i]:
                    loop = False
                    logged = True
                    return logged
        n-=1
        print(f"Invalid Password or Username! Try another one. ({n} more attempt)")
        if n==0:
            print("You lose attempts, please try again later.\n")
            return logged
#########################################################################################################################################

def menu_1():
    print("Info Penting")

def menu_2():
    print("Temperature Detector")
    arr = []
    while result:
        suhu = int(input("Masukkan suhu: "))
            if (suhu > 37):
                arr.append(suhu)
                print("Anda tidak diperbolehkan masuk")
                rata = sum(arr)/(len(arr))
                result = "y" in input("Rata-rata suhu anda:" + str(rata) + " input suhu lagi? (y/n): ").lower() 
            elif (suhu <= 37):
                arr.append(suhu)
                print("Anda diperbolehkan masuk")
                rata = sum(arr)/(len(arr))
                result = "y" in input("Rata-rata suhu anda:" + str(rata) + " input suhu lagi? (y/n): ").lower()

def menu_3():
    print("QR Code")

def menu_4():
    print("Diary Perjalanan")

def menu_5():
    print("Pendaftaran Vaksin")

def menu_invalid():
    print("invalid input. Please enter only 1-5")   

#########################################################################################################################################
def main_menu(logged):
    arr_menu = ["Info Penting", "Temperature Detector", "Scan QR Code", "Diary Perjalanan", "Pendaftaran Vaksin"]
    print()
    items = "list of available functions "
    for e in range(len(items)+2):
        print("=", end="")
    print()
    print("", items)
    for e in range(len(items)+2):
        print("=", end="")
    print()
    for e in range(len(arr_menu)):
        print(str(e+1) + ". " + arr_menu[e])
    print()
    print()
    y = input("Tekan Q Jika ingin keluar: ")
    if y == "Q" or "q":
        z = input("Tekan Q sekali lagi jika ingin keluar: ")
        if z == "Q" or "q":
            logged = False
            print("Thanks for using TempDec ^_^\n")
            return logged
    
    B = int(input("\nChoose one of the above: "))
    if B == 1:
        menu_1()
    elif B == 2:
        menu_2()
    elif B == 3:
        menu_3()
    elif B == 4:
        menu_4()
    elif B == 5:
        menu_5()
    else:
        menu_invalid()

#########################################################################################################################################

while app:
    for e in range(len(welcome)+2):
        print("=", end="")
    print()
    print("", welcome)
    for i in range(len(welcome)+2):
        print("=", end="")
    acc = input("\nAlready have an account? log in to continue! (y/n): ")
    if acc == "y" or acc == "Y":
        logged = login_main(logged)
    elif acc == "n" or acc == "N":
        logged = regis_main(logged)
    while logged:
        logged = main_menu(logged)
    y = input("Do you want to exit? Your process will not be saved (y/n)  :")
    if y == "y":
        exit()

#########################################################################################################################################
