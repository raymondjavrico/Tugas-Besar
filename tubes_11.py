# WELCOME TO TEMPDEC

# bagian 1 (login & register)

# Infinity loop (ga akan pernah selesai) 
# pros: program lebih detail (memudahkan user), bisa log in ke username yg udh diregister sblmmya/switch account (register dgn alamat email, no telp & username baru)
# cons: bikin flowchart & pseudocodenya ribet

from random import randint
arr_name = ["empty"]
arr_email = ["empty"]
arr_phone = [0]
arr_password = ["empty"]
attempt = 0
repeat = False
ngulang = False
gewees = False
result = True
satu = True
daiya = False
welcome = "Welcome to TempDec!"
name = ""
valid = ""

while result:
    for e in range(len(welcome)+2):
        print("=", end="")
    print()
    print("", welcome)
    for i in range(len(welcome)+2):
        print("=", end="")
    acc = input("\nAlready have an account? log in to continue! (y/n): ")
    if acc == "y" or acc == "Y":
        daiya = True
    elif acc == "n" or acc == "N":
        dar = input("Please sign in to use the application! (click ok to continue): ").lower()
        if dar == "ok":
            m = input("TempDec wants to ask for access to your location, files, and camera (click ok to continue): ").lower()
            if m == "ok":
                while satu:
                    email = input("Please enter your email         : ")
                    daiya = True
                    for element in arr_email:
                        if element == email:
                            print("This email address has already been registered into another account. Please choose another one.")
                            ngulang = True
                            daiya = False
                    if daiya:
                        arr_email.append(email)
                        satu = False
                        daiya = False
                while not satu:
                    phone = input("Please enter your phone number  : ")
                    daiya = True
                    for element in arr_phone:
                        if element == phone:
                            print("This phone number has already been registered into another account. Please choose another one.")
                            ngulang = True
                            daiya = False
                    if daiya:
                        arr_phone.append(phone)
                        satu = True
                        daiya = False
                while satu:
                    name = input("Please enter your username      : ")
                    daiya = True
                    for element in arr_name:
                        if element == name:
                            print("This username has already been taken. Please choose another one.")
                            ngulang = True
                            daiya = False
                    if daiya:
                        arr_name.append(name)
                        satu = False
                        daiya = False
                password = input("Please enter your password      : ")
                arr_password.append(password)
                print("Hello, " + name + "!" + " we have sent a code to your device, please insert the code to continue! ")
                repeat = True
            else:
                print("Please click ok to continue.")
                ngulang = False
                daiya = False
        else:
            print("Please click ok to continue.")
            ngulang = False
            daiya = False
    else:
        print("Invalid input. Please enter either y/n.\n")

    while daiya:
        gewees = True
        name = input("Please enter your username      : ")
        password = input("Please enter your password      : ")
        for e in arr_name:
            if e == name:
                valid = "Valid Username! Welcome, " + name
                ngulang = True
        for m in arr_password:
            if m == password and ngulang:
                print(valid)
                gewees = False
                daiya = False
        if gewees:
            print("Invalid Password or Username! Try another one! ")
            attempt += 1
            if attempt == 3:
                print("You lose attempts, please try again later.\n")
                attempt = 0
                gewees = False
                ngulang = False
                daiya = False

    arr = []
    while repeat:
        jia = randint(100, 1000)
        repeat = ("y" or "yes") in input("You received the code: " + str(jia) + ", do you want us to send another code? (y/n): ").lower()
        arr.append(jia)
        daiya = True

    while daiya:
        code = int(input("Insert the code you have received: "))
        if code == arr[len(arr)-1]:
            daiya = False
            memo = input("I accept the privacy and policy terms of this application: ")
            if memo == "y" or memo == "yes":
                print("Congratulations! You have succesfully signed in to TempDec ^_^")
                ngulang = True
                daiya = False

            elif memo == ("n" or "no") in input().lower():
                result = False
        else:
            print("Please enter the latest code.")

# bagian 2 (dalam aplikasi)

    arrey = ["Info Penting", "Temperature Detector", "Scan QR Code", "Diary Perjalanan", "Pendaftaran Vaksin"]
    if ngulang:
        print()
        items = "list of available functions "
        for i in range(len(items)+2):
            print("=", end="")
        print()
        print("", items)
        for i in range(len(items)+2):
            print("=", end="")
            gewees = True
    while gewees:
        print()
        for e in range(len(arrey)):
            print(str(e+1) + ". " + arrey[e])
        B = int(input("\nChoose one of the above: "))
        if B == 1:
            info = "\nBla bla bla fafifu was wes wos pokoknya ini informasi penting banget jadi tempdec ini itu \n" \
                "seperti semacam aplikasi dimana kamu bisa .... dan bisa ngecek temperatur juga tapi di sini cuma \n" \
                "kurang lebih simulasi doang ga ngecek beneran, terus bisa scan QR code juga untuk mengetahui apakah \n" \
                "kita bisa masuk ke suatu tempat atau tidak. Ada juga diary perjalanan untuk mengetahui tempat \n" \
                "apa saja yang sudah kita kunjungi, dan terdapat juga pendaftaran vaksin."
            print(info)
            back = input("\nDo you want to go back? (y/n): ")
            if back == "y" or back == "Y":
                gewees = True
            else:
                print("Thanks for using TempDec ^_^\n")
                attempt = 0
                satu = True
                gewees = False
    # Bagian B = 2-5 kalian isi langsung sesuai pembagian tugasnya ya gais, jadi
    # 2 = Temperature Detector
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
            result != "n"
    # 3 = Scan QR Code
    # 4 = Diary Perjalanan
    # 5 = Pendaftaran Vaksin
        elif B == 2:
            print("Temperature Detector")
        elif B == 3:
            print("QR Code")
        elif B == 4:
            print("Diary Perjalanan")
            print("Belum ada data terkait riwayat lokasi perjalanan Anda")
        elif B == 5:
            print("Pendaftaran Vaksin")
        else:
            print("invalid input. Please enter only 1-5.")
