
# WELCOME TO TEMPDEC

# bagian 1 (login & register)

from random import randint

welcome = "Welcome to TempDec!"
for i in range(len(welcome)+2):
    print("=", end="")
print()
print("", welcome)
for i in range(len(welcome)+2):
    print("=", end="")

repeat = True
m = input("\n" + "TempDec wants to ask for access to your location, files, and camera (click ok to continue): ")
if m == "ok" or m == "Ok" or m == "OK" or m == "oK":
    name = input("Please enter your username      : ")
    phone = int(input("Please enter your phone number  : "))
    email = input("Please enter your email         : ")
    print("Hello, " + name + "!" + " we have sent a code to your device, please insert the code to continue! ")
else:
    repeat = False

# aslinya sebelum ini ada hiasan dikit gitu, nama no. telp & email di border tapi nanti aja lah

result = True
arr = []
while repeat:
    jia = randint(100, 1000)
    print("You received the code: " + str(jia) + ", do you want us to send another code?")
    arr.append(jia)
    repeat = ("y" or "yes") in input().lower()
    result = False

while not result:
    code = int(input("Insert the code you have received: "))
    if code == arr[len(arr)-1]:
        result = True
        repeat = True
    else:
        print("Please enter the latest code.")

if repeat and result:
    memo = input("I accept the privacy and policy terms of this application: ")
    if memo == "y" or memo == "yes":
        print("Congratulations! You have succesfully signed in to TempDec ^_^")

    elif memo == ("n" or "no") in input().lower():
        repeat = False

# bagian 2 (dalam aplikasi)

arrey = ["Info Penting", "Pendaftaran Vaksin", "Scan QR Code", "Diary Perjalanan", "Paspor Digital"]
gewees = False
if repeat:
    print()
    items = "list of available functions "
    for i in range(len(items)+2):
        print("=", end="")
    print()
    print("", items)
    for i in range(len(items)+2):
        print("=", end="")
    print("\n")
    gewees = True
while gewees:
    for e in range(len(arrey)):
        print(str(e+1) + ". " + arrey[e])
    B = int(input("Choose one of the above: "))
    if B == 1:
        info = "Bla bla bla fafifu was wes wos pokoknya ini informasi penting banget jadi tempdec ini itu \n " \
            "seperti semacam aplikasi dimana kamu bisa .... dan bisa ngecek temperatur juga tapi di sini cuma kurang lebih \n " \
            "simulasi doang ga ngecek beneran, terus bisa scan qr code juga untuk mengetahui apakah kita bisa masuk ke suatu \n " \
            "tempat atau tidak kurang lebih kayak gitu sih sistemnya. Sama ada paspor digital untuk mengetahui apakah kita udah \n" \
            "vaksin apa belum sm ada pendaftarannya juga, terus diary perjalanan juga ada."
        print(info)
        back = input("Do you want to go back? (y/n): ")
        if back == "y" or back == "Y":
            gewees = True
        else:
            gewees = False
    elif B == 2:
        c = input("Apakah kamu ingin mendaftar vaksin? (y/n): ")
        if c == "y" or c == "Y":
            nama = input("Masukkan nama: ")


# ntar diganti aja jadi table

# 1.Do you want to install this application? (Yes/No)
# 2.Bakal minta akses ke lokasi, penyimpanan, dan kamera
# 3.Registrasi (input No. Hp & email)
# 4.Random randint buat nomor OTP
# 5.Tekan kolom Saya menerima isi syarat penggunaan dan kebijakan privasi
# 6.“Selamat anda berhasil masuk”
# 7.Ntar ada array isinya ‘Pendaftaran Vaksin’, ‘Scan QR Code’, ‘Teledokter’, ‘Info Penting’, ‘Diary Perjalanan’, dan ‘Paspor Digital’. (boleh diilangin beberapa)
# 8. Pilih salah satu dr itu, next
