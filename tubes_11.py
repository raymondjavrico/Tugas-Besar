# WELCOME TO TEMPDEC
# Bacanya dari paling bawah

from datetime import datetime
from PIL import Image
from pyzbar.pyzbar import decode
from random import randint
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import track
import qrcode
import time
logged = False
app = True
arr_name = ["empty"]
arr_email = ["empty"]
arr_suhu = []
arr_phone = [0]
arr_password = ["empty"]
arr_location = []
arr_datetime = []
MARKDOWN1 = """
# Welcome to TempDec
"""
MARKDOWN2 = """
# Temperature Detector 
"""
MARKDOWN3 = """
# QR Code 
"""
MARKDOWN5 = """
# Pendaftaran Vaksin 
"""
MARKDOWN = """
# Info Penting 
"""
MARKDOWN4 = """
# Diary Perjalanan 
## Belum ada Data Terkait Riwayat Perjalanan Anda
"""
MARKDOWN44 = """
# Diary Perjalanan 
"""

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
    console = Console()
    loop = True
    global arr_email, email
    while loop:
        email = input("Please enter your email          : ")
        confirm = True
        for element in arr_email:
            if element == email:
                confirm = False
                console.print("[bold red]This email address has already been registered into another account. "
                              "Please choose another one.[bold red]")
        if confirm:
            arr_email.append(email)
            loop = False
    return  # balek ke regis_main()


def regis_phone():
    loop = True
    console = Console()
    global arr_phone
    while loop:
        phone = int(input("Please enter your phone number   : "))
        confirm = True
        for element in arr_phone:
            if element == phone:
                confirm = False
                console.print("[bold red]This phone number has already been registered into another account. "
                              "Please choose another one.[bold red]")
        if confirm:
            arr_phone.append(phone)
            loop = False
    return  # balek ke regis_main()


def regis_username():
    loop = True
    global arr_name, arr_password, username
    while loop:
        confirm = True
        username = input("Please enter your username       : ")
        for element in arr_name:
            if element == username:
                confirm = False
                console = Console()
                console.print("[bold red]This username has already been taken. Please choose another one.[bold red]")
        if confirm:
            arr_name.append(username)
            loop = False
    password = input("Please enter your password       : ")
    arr_password.append(password)
    return  # balek ke regis_main()


def regis_otp():
    arr_otp = []
    loop = True
    console = Console()
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
            console.print("Please enter the latest code.", style="italic cyan")
    return


def regis_agree():
    loop = True
    console = Console()
    while loop:
        loop = ("y" or "yes" or "ok" or "oke") in input(
            "I accept the privacy and policy terms of this application (y/n): ").lower()
        if loop:
            console.print("[bold]Congratulations! You have successfully signed in to TempDec[/bold] :smiley:")
            loop = False
        else:
            console.print("You must agree to the privacy and policy terms of this application to continue using this app.", style="italic cyan")
            loop = True
    return


#########################################################################################################################################
def regis_main(logged):
    reg = input("Please register in to use the program! (click ok to continue): ").lower()
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
    global arr_name, arr_password, arr_location, arr_datetime, arr_suhu
    loop = True
    n = 5
    console = Console()
    while loop:
        name = input("Please enter your username       : ")
        password = input("Please enter your password       : ")
        i = -1
        for e in range(len(arr_name)):
            i += 1
            if name == arr_name[e]:
                if e != (len(arr_name)-1):
                    arr_location = []
                    arr_datetime = []
                    arr_suhu = []
                if password == arr_password[i]:
                    loop = False
                    logged = True
                    return logged  # balik ke main()
        n -= 1
        console.print(f"[bold]Invalid Password [italic]or[/italic] Username! Try another one. [red]({n} more attempt)")
        if n == 0:
            console.print("[underline red bold]You [italic]lose[/] attempts[/], [bold]please try again later.\n")
            return logged  # balik ke main()


#########################################################################################################################################

def menu_1():
    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)
    info = "\nTempDec adalah program yang dapat melakukan pendataan dan pelacakan untuk menghentikan penyebaran Coronavirus Disease (COVID-19)." \
           "Adanya fitur temperature detector dapat menunjukkan apakah anda diperbolehkan masuk ke ruang publik atau tidak sesuai " \
           "keadaan suhu tubuh anda saat itu dan anda dapat melihat suhu rata-rata tubuh anda dari beberapa pengecekan yang telah dilakukan sebelumnya. " \
           "Fitur QR Code akan membantu untuk mendata dan mendapatkan informasi lokasi anda saat memasuki ruang publik. " \
           "Terdapat fitur diary perjalanan yang dapat mengetahui tempat mana saja yang pernah dikunjungi sebelumnya. " \
           "Ada juga fitur pendaftaran vaksin yang dapat memudahkan dalam pendataan informasi dan jadwal pendaftaran vaksin yang" \
           " dapat disesuaikan oleh pengguna TempDec."
    console.print(info, justify="full")
    back()
    return  # balik ke main_menu()


def menu_2():
    loop = True
    console = Console()
    md = Markdown(MARKDOWN2)
    console.print(md)
    while loop:
        suhu = float(input("\nMasukkan suhu: "))
        arr_suhu.append(suhu)
        rata = sum(arr_suhu) / (len(arr_suhu))
        if (suhu > 37):
            print("Anda tidak diperbolehkan masuk")
        else:
            print("Anda diperbolehkan masuk")
        loop = "y" in input("Rata-rata suhu anda: " + str(rata) + " input suhu lagi? (y/n): ").lower()
    return  # balik ke main_menu()


def menu_3():
    console = Console()
    md = Markdown(MARKDOWN3)
    console.print(md)
    global username, email, arr_location, arr_datetime
    location = input("\nWhere do you want to check in?  :  ")
    arr_location.append(location)
    img = qrcode.make(f"Username: {username}\n"
                      f"Email Address: {email}\n"
                      f"Lokasi Check-In: {location}\n"
                      f"Tanggal & Waktu Check-In: {datetime.now()}\n"
                      f"Selamat, Anda berhasil Check-In ^_^")
    img.save("random.png")
    arr_datetime.append(str(datetime.now()))
    d = decode(Image.open("random.png"))
    for i in track(range(5), description="processing..."):
        time.sleep(0.2)
        if i == 4:
            with Image.open("random.png") as img:
                img.show()
            print(d[0].data.decode('ascii'))
    back()
    return  # balik ke main_menu()


def menu_4():
    global arr_location, arr_datetime
    console = Console()
    table = Table(title="", style="cyan")
    table.add_column("Lokasi Check-In", style="aquamarine1", justify="center")
    table.add_column("Tanggal & Waktu Check-In", style="magenta")
    repeat = False
    if len(arr_location) > 0:
        md = Markdown(MARKDOWN44)
        console.print(md)
        for e in range(len(arr_location)):
            table.add_row(f"{arr_location[e]}", f"{arr_datetime[e]}")
            repeat = True
    else:
        md = Markdown(MARKDOWN4)
        console.print(md)
    if repeat:
        console.print(table)
    back()
    return  # balik ke main_menu()


def menu_5():
    console = Console()
    md = Markdown(MARKDOWN5)
    console.print(md)
    keterangan_vaksin = input(
        'Keterangan vaksin: ').lower()  # isi dengan belum vaksin atau sudah vaksin pertama atau sudah vaksin kedua
    if keterangan_vaksin == 'belum vaksin' or keterangan_vaksin == 'sudah vaksin pertama':  # pendaftaran vaksin bisa dilakukan
        # identitas diri
        print('\nJika ingin divaksin, silakan isi data diri berikut \nIDENTITAS DIRI')
        # masukkan data diri user
        nama_lengkap = input('Nama lengkap: ')  # nama lengkap sesuai KTP
        NIK = input('NIK: ')  # NIK adalah Nomor Induk Kependudukan
        jenis_kelamin = ['laki-laki', 'perempuan']
        indeks_jenis_kelamin = int(
            input('Masukkan indeks jenis kelamin: '))  # indeks 0 (laki-laki) dan indeks 1 (perempuan)
        print(f'Jenis kelamin: {jenis_kelamin[indeks_jenis_kelamin]}')
        tanggal_lahir = input('Tanggal lahir: ')  # format tanggal lahir: 11/04/1995
        usia = float(input('Usia: '))  # usia saat ini dalam tahun
        nomor_HP = input('Nomor HP: ')
        nomor_telepon_rumah = input('Nomor telepon rumah: ')
        email = input('Email: ')

        # alamat
        print('\nALAMAT')
        # masukan alamat user
        alamat = input('Alamat: ')  # alamat berdasarkan KTP
        alamat_sekarang = input('Alamat sekarang: ')

        # jadwal vaksin
        print('\nJADWAL VAKSIN')
        # masukan jadwal vaksin dari user
        tanggal_vaksin = input(
            'Masukkan tanggal vaksin yang Anda inginkan: ')  # asumsikan tanggal yang di-input adalah benar # formatnya: 28 Oktober 2021
        waktu_vaksin = ['09:00-11:00 WIB', '13:00-15:00 WIB', '16:00-18:00 WIB']
        indeks_waktu = int(input('Masukkan indeks waktu: '))  # asumsikan hanya terdapat 3 waktu vaksin
        # indeks 0 untuk 09:00-11:00 WIB
        # indeks 1 untuk 13:00-15:00 WIB
        # indeks 2 untuk 16:00-18:00 WIB
        print(f'Waktu vaksin yang Anda pilih adalah {waktu_vaksin[indeks_waktu]}')
        lokasi_vaksin = ['puskesmas', 'aula', 'rumah sakit']
        indeks_lokasi = int(input('Masukkan indeks lokasi: '))  # asumsikan hanya terdapat 3 lokasi vaksin
        # indeks 0 untuk puskesmas
        # indeks 1 untuk aula
        # indeks 2 untuk rumah sakit
        print(f'Lokasi vaksin yang Anda pilih adalah {lokasi_vaksin[indeks_lokasi]}')

        # output setelah selesai mengisi semua data
        print('\nPendaftaran vaksin telah berhasil')

    else:  # sudah vaksin kedua
        print('\nAnda telah divaksin sebanyak dua kali dan tidak bisa mendaftar lagi')
    back()
    return  # balik ke main_menu()


def menu_invalid():
    print("invalid input. Please enter only 0-5")
    back()
    return  # balik ke main_menu()


#########################################################################################################################################

def main_menu(logged):
    global arr_suhu, arr_location
    logged_menu = True
    while logged_menu:
        print()
        console = Console()
        table1 = Table(title="")
        table1.add_column("", style="aquamarine1")
        table1.add_column("Fitur yang Tersedia", style="cornsilk1", justify="left")
        arr_menu = ["Info Penting", "Temperature Detector", "Scan QR Code", "Diary Perjalanan", "Pendaftaran Vaksin", "Exit"]
        for e in range(len(arr_menu)):
            if e == (len(arr_menu)-1):
                table1.add_row(f'0', f"{arr_menu[e]}")
                break
            else:
                table1.add_row(f"{e+1}", f"{arr_menu[e]}")
        console.print(table1)
        B = int(input("\nPilih salah satu dari nomor di atas: "))
        if B == 0:
            z = str(input("Tekan 0 sekali lagi jika ingin sign out (Apabila switch account, data suhu dan lokasi anda "
                          "tidak akan terekam saat kembali log in): "))
            if z == "0":
                logged = False
                logged_menu = False
                console.print("Thanks for using TempDec :thumbs_up:\n")
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
    global logged, arr_suhu, arr_location, arr_datetime
    console = Console()
    while app:
        print()
        md = Markdown(MARKDOWN1)
        console.print(md)
        acc = input("\nAlready have an account? log in to continue! (y/n): ")
        if acc == "y" or acc == "Y":
            logged = login_main(logged)
        elif acc == "n" or acc == "N":
            arr_suhu = []
            arr_datetime = []
            arr_location = []
            logged = regis_main(logged)
        while logged:
            logged = main_menu(logged)
        y = input("Do you want to exit? Exiting will terminate the program (y/n): ")
        if y == "y":
            exit()


#########################################################################################################################################
main()
