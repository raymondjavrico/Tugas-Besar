# WELCOME TO TEMPDEC
#Bacanya dari paling bawah

from random import randint

logged = False
app = True
arr_name = ["empty"]
arr_email = ["empty"]
arr_suhu = []
arr_phone = [0]
arr_password = ["empty"]

def title_screen(title):
    for e in range(len(title) + 2):
        print("=", end="")
    print()
    print("", title)
    for e in range(len(title) + 2):
        print("=", end="")
    print()
    return  # balek ke apapun yang butuh title screen


def back():
    loop = False
    while not loop:
        balik = input("\nPress y to go back: ")
        if balik == "y".lower() or balik == "yes".lower():
            loop = True
        else:
            print("Invalid input.")
    return  # balek ke apapun yang butuh back


def regis_email():
    loop = True
    global arr_email
    while loop:
        email = input("Please enter your email          : ")
        confirm = True
        for element in arr_email:
            if element == email:
                confirm = False
                print("This email address has already been registered into another account. Please choose another one.")
        if confirm:
            arr_email.append(email)
            loop = False
    return  # balek ke regis_main()


def regis_phone():
    loop = True
    global arr_phone
    while loop:
        phone = int(input("Please enter your phone number   : "))
        confirm = True
        for element in arr_phone:
            if element == phone:
                confirm = False
                print("This phone number has already been registered into another account. Please choose another one.")
        if confirm:
            arr_phone.append(phone)
            loop = False
    return  # balek ke regis_main()


def regis_username():
    loop = True
    global arr_name, arr_password
    while loop:
        username = input("Please enter your username       : ")
        confirm = True
        for element in arr_name:
            if element == username:
                confirm = False
                print("This username has already been taken. Please choose another one.")
        if confirm:
            arr_name.append(username)
            loop = False
    password = input("Please enter your password       : ")
    arr_password.append(password)
    return  # balek ke regis_main()


def regis_otp():
    arr_otp = []
    loop = True
    while loop:
        otp = randint(100, 1000)
        loop = ("y" or "yes") in input(
            "You received the code: " + str(otp) + ", do you want us to send another code? (y/n): ").lower()
        arr_otp.append(otp)
    loop = True
    while loop:
        code = int(input("Insert the code you have received: "))
        if code == arr_otp[len(arr_otp) - 1]:
            loop = False
        else:
            print("Please enter the latest code.")
    return


def regis_agree():
    loop = True
    while loop:
        loop = ("y" or "yes" or "ok" or "oke") in input(
            "I accept the privacy and policy terms of this application (y/n): ").lower()
        if loop:
            print("Congratulations! You have succesfully signed in to TempDec ^_^")
            loop = False
        else:
            print("You must agree to the privacy and policy terms of this application to continue using this app.")
            loop = True
    return


#########################################################################################################################################
def regis_main(logged):
    reg = input("Please register in to use the application! (click ok to continue): ").lower()
    if reg == "ok":
        m = input(
            "TempDec wants to ask for access to your location, files, and camera (click ok to continue): ").lower()
        if m == "ok":
            regis_email()
            regis_phone()
            regis_username()
            regis_otp()
            regis_agree()
            logged = True
            return logged  # balik ke main()


#########################################################################################################################################
def login_main(logged):
    global arr_name, arr_password
    loop = True
    n = 5
    while loop:
        name = input("Please enter your username       :")
        password = input("Please enter your password    :")
        i = -1
        for e in arr_name:
            i += 1
            if name == e:
                if password == arr_password[i]:
                    loop = False
                    logged = True
                    return logged  # balik ke main()
        n -= 1
        print(f"Invalid Password or Username! Try another one. ({n} more attempt)")
        if n == 0:
            print("You lose attempts, please try again later.\n")
            return logged  # balik ke main()


#########################################################################################################################################

def menu_1():
    title_screen("Info penting")
    info = "\nBla bla bla fafifu was wes wos pokoknya ini informasi penting banget jadi tempdec ini itu \n" \
           "seperti semacam aplikasi dimana kamu bisa .... dan bisa ngecek temperatur juga tapi di sini cuma \n" \
           "kurang lebih simulasi doang ga ngecek beneran, terus bisa scan QR code juga untuk mengetahui apakah \n" \
           "kita bisa masuk ke suatu tempat atau tidak. Ada juga diary perjalanan untuk mengetahui tempat \n" \
           "apa saja yang sudah kita kunjungi, dan terdapat juga pendaftaran vaksin."
    print(info)
    back()
    return  # balik ke main_menu()


def menu_2():
    loop = True
    title_screen("Temperature Detector")
    while loop:
        suhu = int(input("\nMasukkan suhu: "))
        arr_suhu.append(suhu)
        if (suhu > 37):
            print("Anda tidak diperbolehkan masuk")
            rata = sum(arr_suhu) / (len(arr_suhu))
            loop = "y" in input("Rata-rata suhu anda: " + str(rata) + " input suhu lagi? (y/n): ").lower()
        else:
            print("Anda diperbolehkan masuk")
            rata = sum(arr_suhu) / (len(arr_suhu))
            loop = "y" in input("Rata-rata suhu anda: " + str(rata) + " input suhu lagi? (y/n): ").lower()
    return  # balik ke main_menu()


def menu_3():
    title_screen("QR Code")
    back()
    return  # balik ke main_menu()


def menu_4():
    title_screen("Diary Perjalanan")
    back()
    return  # balik ke main_menu()


def menu_5():
    title_screen("Pendaftaran Vaksin")
    # fitur "Pendaftaran Vaksin"

    # masukan keterangan vaksin
    keterangan_vaksin = input('Keterangan vaksin: ') # isi dengan belum vaksin atau sudah vaksin pertama atau sudah vaksin kedua

    # percabangan untuk menentukan apakah user boleh divaksin atau tidak
    if keterangan_vaksin == 'belum vaksin' or keterangan_vaksin == 'sudah vaksin pertama': # pendaftaran vaksin bisa dilakukan
    
        print('\nJika ingin divaksin, silakan isi data diri berikut')
        # identitas diri
        print('\nIDENTITAS DIRI')
        # masukan data diri user
        nama_lengkap = input('Nama lengkap: ') # nama lengkap sesuai KTP
        NIK = input('NIK: ') # NIK adalah Nomor Induk Kependudukan
        jenis_kelamin = ['laki-laki','perempuan']
        indeks_jenis_kelamin = int(input('Masukkan indeks jenis kelamin: ')) # indeks 0 (laki-laki) dan indeks 1 (perempuan)
        print(f'Jenis kelamin: {jenis_kelamin[indeks_jenis_kelamin]}')
        tanggal_lahir = input('Tanggal lahir: ') # format tanggal lahir: 11/04/1995
        usia = float(input('Usia: ')) # usia saat ini dalam tahun
        nomor_HP = input('Nomor HP: ') 
        nomor_telepon_rumah = input('Nomor telepon rumah: ')
        email = input('Email: ')

        # alamat
        print('\nALAMAT')
        # masukan alamat user
        alamat = input('Alamat: ') # alamat berdasarkan KTP
        alamat_sekarang = input('Alamat sekarang: ')

        # jadwal vaksin
        print('\nJADWAL VAKSIN')
        # masukan jadwal vaksin dari user
        tanggal_vaksin = input('Masukkan tanggal vaksin yang Anda inginkan: ') # asumsikan tanggal yang di-input adalah benar # formatnya: 28 Oktober 2021 
        waktu_vaksin = ['09:00-11:00 WIB', '13:00-15:00 WIB', '16:00-18:00 WIB']
        indeks_waktu = int(input('Masukkan indeks waktu: ')) # asumsikan hanya terdapat 3 waktu vaksin
        # indeks 0 untuk 09:00-11:00 WIB
        # indeks 1 untuk 13:00-15:00 WIB
        # indeks 2 untuk 16:00-18:00 WIB
        print(f'Waktu vaksin yang Anda pilih adalah {waktu_vaksin[indeks_waktu]}')
        lokasi_vaksin = ['puskesmas', 'aula', 'rumah sakit']
        indeks_lokasi = int(input('Masukkan indeks lokasi: ')) # asumsikan hanya terdapat 3 lokasi vaksin
        # indeks 0 untuk puskesmas
        # indeks 1 untuk aula
        # indeks 2 untuk rumah sakit
        print(f'Lokasi vaksin yang Anda pilih adalah {lokasi_vaksin[indeks_lokasi]}')

        # output setelah selesai mengisi semua data
        print('\nPendaftaran vaksin telah berhasil')

else: # sudah vaksin kedua
    print('\nAnda telah divaksin sebanyak dua kali dan tidak bisa mendaftar lagi')
    back()
    return  # balik ke main_menu()


def menu_invalid():
    print("invalid input. Please enter only 1-5")
    back()
    return  # balik ke main_menu()


#########################################################################################################################################

def main_menu(logged):
    logged_menu = True
    while logged_menu:
        arr_menu = ["Info Penting", "Temperature Detector", "Scan QR Code", "Diary Perjalanan", "Pendaftaran Vaksin"]
        print()
        items = "List of available function"
        title_screen(items)
        print()
        for e in range(len(arr_menu)):
            print(str(e + 1) + ". " + arr_menu[e])
        print("0. exit")
        B = int(input("\nPilih salah satu dari nomor di atas: "))
        if B == 0:
            z = str(input("Tekan 0 sekali lagi jika ingin sign out: "))
            if z == "0":
                logged = False
                logged_menu = False
                print("Thanks for using TempDec ^_^\n")
                return logged  # balik ke main()
        elif B == 1:
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

def main():
    app = True
    global logged
    while app:
        title_screen("Welcome to TempDec")
        acc = input("\nAlready have an account? log in to continue! (y/n): ")
        if acc == "y" or acc == "Y":
            logged = login_main(logged)
        elif acc == "n" or acc == "N":
            logged = regis_main(logged)
        while logged:
            logged = main_menu(logged)
        y = input("Do you want to exit? Your process will not be saved (y/n): ")
        if y == "y":
            exit()


#########################################################################################################################################
main()
