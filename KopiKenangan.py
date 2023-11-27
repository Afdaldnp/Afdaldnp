import random
import datetime

total = []
ukuran = []
nama = []
toping = []
namaToping = []
banyak = []
namaPembeli = input("Masukan Nama Pembeli : ")

def ArabicaBlend():
    print("-"*60)
    print("{:^60}".format("Arabica Blend "))
    print("-"*60)
    print("No  | {:^30} | {:^22}".format("Nama Menu", " Ukuran"))
    print("{:^38} {:^10} | {:^10}".format(" ", "R", "L"))
    print("-"*60)
    print("1   | {:<30} | {:^10} | {:^10}".format("Kopi Kenangan Mantan", "18000", "24000"))
    print("2   | {:<30} | {:^10} | {:^10}".format("Due Shot Iced Shaken", "22000", "28000"))
    print("3   | {:<30} | {:^10} | {:^10}".format("Latte", "18000", "24000"))
    print("4   | {:<30} | {:^10} | {:^10}".format("Kopi Dolce", "20000", "26000"))
    print("5   | {:<30} | {:^10} | {:^10}".format("Cappuccino", "18000", "25000"))
    print("6   | {:<30} | {:^10} | {:^10}".format("Americano", "15000", "19000"))
    print("7   | {:<30} | {:^10} | {:^10}".format("Kopi Kelapa", "19000", "25000"))
    print("8   | {:<30} | {:^10} | {:^10}".format("Caramel Macchiato", "28000", "36000"))
    print("9   | {:<30} | {:^10} | {:^10}".format("Mocha Latte", "28000", "38000"))
    print("10  | {:<30} | {:^10} | {:^10}".format("Avocado Coffee", "24000", "32000"))
    print("11  | {:<30} | {:^10} | {:^10}".format("Caramel Latte", "24000", "34000"))
    print("-"*60)
    a = int(input("Masukan Menu yang dipesan        : "))
    if a == 1:
        nama.append("Kopi Kenangan Mantan")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 18000
        elif b == "L" or b == "l":
            Total = 24000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 2:
        nama.append("Due Shot Iced Shaken")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 22000
        elif b == "L" or b == "l":
            Total = 28000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 3:
        nama.append("Latte")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 18000
        elif b == "L" or b == "l":
            Total = 24000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 4:
        nama.append("Kopi Dolce")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 20000
        elif b == "L" or b == "l":
            Total = 26000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 5:
        nama.append("Cappuccino")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 18000
        elif b == "L" or b == "l":
            Total = 25000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 6:
        nama.append("Americano")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 15000
        elif b == "L" or b == "l":
            Total = 19000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 7:
        nama.append("Kopi Kelapa")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 19000
        elif b == "L" or b == "l":
            Total = 25000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 8:
        nama.append("Caramel Macchiato")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 28000
        elif b == "L" or b == "l":
            Total = 36000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 9:
        nama.append("Mocha Latte")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 28000
        elif b == "L" or b == "l":
            Total = 38000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 10:
        nama.append("Avocado Coffee")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 24000
        elif b == "L" or b == "l":
            Total = 32000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 11:
        nama.append("Caramel Latte")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 24000
        elif b == "L" or b == "l":
            Total = 34000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    if a >= 1 and a <= 11:
        total.append(Total*jumlah)
        ukuran.append(b)
        banyak.append(jumlah)
        tanya()
    else:
        print("Menu yang anda masukan tidak tersedia!! silakan masukan ulang")
        ArabicaBlend()
    
def MilkTea():
    print("-"*60)
    print("{:^60}".format("Milk Tea"))
    print("-"*60)
    print("No  | {:^30} | {:^23}".format("Nama Menu", " Ukuran"))
    print("{:^38} {:^10} | {:^10}".format(" ", "R", "L"))
    print("-"*60)
    print("1   | {:<30} | {:^10} | {:^10}".format("Kenangan Milk Tea", "18000", "24000"))
    print("2   | {:<30} | {:^10} | {:^10}".format("Jasminan Milk Tea", "18000", "24000"))
    print("3   | {:<30} | {:^10} | {:^10}".format("Hazelnut Milk Tea", "22000", "28000"))
    print("4   | {:<30} | {:^10} | {:^10}".format("Thai Tea", "15000", "18000"))
    print("5   | {:<30} | {:^10} | {:^10}".format("Kenangan Matcha Indah", "24000", "29000"))
    print("6   | {:<30} | {:^10} | {:^10}".format("Hajicha Latte", "24000", "29000"))
    print("-"*60)
    a = int(input("Masukan Menu Yang Dipilih        : "))
    if a == 1:
        nama.append("Kenangan Milk Tea")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 18000
        elif b == "L" or b == "l":
            Total = 24000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 2:
        nama.append("Jasminan Milk Tea")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 18000
        elif b == "L" or b == "l":
            Total = 24000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 3:
        nama.append("Hazelnut Milk Tea")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 22000
        elif b == "L" or b == "l":
            Total = 28000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 4:
        nama.append("Thai Tea")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 15000
        elif b == "L" or b == "l":
            Total = 18000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 5:
        nama.append("Kenangan Matcha Indah")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 24000
        elif b == "L" or b == "l":
            Total = 29000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 6:
        nama.append("Hajicha Latte")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 24000
        elif b == "L" or b == "l":
            Total = 29000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    if a >= 1 and a <= 6:
        total.append(Total*jumlah)
        ukuran.append(b)
        banyak.append(jumlah)
        tanya()
    else:
        print("Menu yang anda masukan tidak tersedia!! silakan masukan ulang")
        MilkTea()
                
    
def TeaBlend():
    print("-"*60)
    print("{:^60}".format("Tea Blend"))
    print("-"*60)
    print("No  | {:^30} | {:^22}".format("Nama Menu", "Ukuran"))
    print("{:^38} {:^10} | {:^10}".format(" ", "R", "L"))
    print("-"*60)
    print("1   | {:<30} | {:^10} | {:^10}".format("Jasmine Earl Grey Tea", "15000", "18000"))
    print("2   | {:<30} | {:^10} | {:^10}".format("Lemon Black Tea", "18000", "24000"))
    print("3   | {:<30} | {:^10} | {:^10}".format("Rasberry Lemon Tea", "20000", "28000"))
    print("-"*60)
    a = int(input("Masukan Menu Yang Dipilih        : "))
    if a == 1:
        nama.append("Jasmine Earl Grey Tea")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 15000
        elif b == "L" or b == "l":
            Total = 18000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 2:
        nama.append("Lemon Black Tea")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 18000
        elif b == "L" or b == "l":
            Total = 24000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    elif a == 3:
        nama.append("Rasberry Lemon Tea")
        b = input("Masukan Ukuran Yang Dipilih      : ")
        if b == "R" or b == "r":
            Total = 22000
        elif b == "L" or b == "l":
            Total = 28000
        jumlah = int(input("Masukan Jumlah Yang Dipesan      : "))
    if a >= 1 and a <= 3:
        total.append(Total*jumlah)
        ukuran.append(b)
        banyak.append(jumlah)
        tanya()
    else:
        print("Menu yang anda masukan tidak tersedia!! silakan masukan ulang")
        TeaBlend()


def menu():
    print("-"*60)
    print("{:^60}".format("KOPI KENANGAN"))
    print("-"*60)
    print("Paket Menu Kopi Kenangan : ")
    print("1. Arabica Blend ")
    print("2. Milk Tea ")
    print("3. Tea Blend ")
    print("-"*60)
    a = int(input("Masukan Paket Menu Yang Dipilih  : "))
    if a == 1:
        ArabicaBlend()
    elif a == 2:
        MilkTea()
    elif a == 3:
        TeaBlend()
    else:
        print("Menu TidaK Ditemukan!! Silakan Pilih Ulang")
        menu()


def tanya():
    print("-"*60)
    tambahan = input("Ingin Tambah Toping [y/t]     : ")
    if tambahan == "y" or tambahan == "Y":
        Toping()
    else:
        toping.append(0)
        namaToping.append(0)
    tanya = input("Ingin tambah Barang [y/t]     : ")
    print("-"*60)
    if tanya == "y" or tanya == "Y":
        menu()
    elif tanya == "t" or tanya == "T":
        bayar()
    else:
        print("Pilihan yang anda masukan salah!")


def Toping():
    print("-"*40)
    print("{:^40}".format("TOPING "))
    print("-"*40)
    print("No  | {:^20} | {:^12}".format("Nama Menu", "Harga"))
    print("-"*40)
    print("1   | {:<20} | {:^10}".format("Boba", "6000"))
    print("2   | {:<20} | {:^10}".format("Jelly", "6000"))
    print("3   | {:<20} | {:^10}".format("Keju", "6000"))
    print("4   | {:<20} | {:^10}".format("Oreo", "6000"))
    print("5   | {:<20} | {:^10}".format("Marie Regal", "6000"))
    a = int(input("Masukan Menu Yang Dipilih     : "))
    if a > 0 and a <= 6:
        toping.append(6000)
    else:
        print("Toping tidak tersedia")
    
    if a == 1:
        namaToping.append("Boba")
    elif a == 2:
        namaToping.append("Jelly")
    elif a == 3:
        namaToping.append("Keju")
    elif a == 4:
        namaToping.append("Oreo")
    elif a == 5:
        namaToping.append("Marie Regal")
    
def bayar():
    global subtotal
    global pajak
    global total_minuman
    global cash
    global kembalian
    
    subtotal = sum(total)+sum(toping)
    pajak = int(subtotal * 0.10)
    total_minuman = int(subtotal + pajak)
    print("-"*40)
    print("{:^40}".format("PEMBAYARAN"))
    print("-"*40)
    print("{:<21} : {:,}".format("subtotal", total_minuman))
    cash = int(input("Masukan Nominal Bayar : "))
    print("-"*40)
    kembalian = cash -  total_minuman
    if cash > total_minuman:
        akhir()
    elif cash < total_minuman:
        print("Uang Yang anda Masukan Kurang!! Silakan coba sekali lagi")
        bayar()



def akhir(): 
    print("-"*45)
    print("{:^45}".format("KOPI KENANGAN"))
    print("{:^45}".format("Artha Loka Kaliabang\n"))
    print("{:^45}\n".format(namaPembeli))
    print("ID order :",random.randrange(100000000, 1000000000), "{:>24}".format("Cashier: Afdal"))
    print(datetime.datetime.now())
    print("-"*45)
    for i in range(len(nama)):
        print("{:<3}{:<22} -{:<8} : {:5,}".format(banyak[i],nama[i], str(ukuran[i]).upper() , total[i]))
        if toping[i] != 0 and toping[i] != 0:
            print("             - {:<20} : {:5,}".format(namaToping[i], toping[i]))
    print("")
    print("{:<35} : {:,}".format("Subotal",sum(total)+sum(toping)))
    print("{:<35} : {:,}".format("PB1",pajak))
    print("{:<35} : {:,}".format("Total",total_minuman))
    print("{:<35} : {:,}".format("CASH",cash))
    print("{:<35} : {:,}".format("CHANGE",kembalian))
    print("-"*45)
    print("{:^45}".format("Terima Kasih"))
    print("{:^45}".format("Selamat Menikmati :) "))
    print("-"*45)
    print("{:^45}".format("Kenangan manis yang sudah tidak ada"))
    print("{:^45}".format("Tapi suka datang tiba tiba dipikiran"))
    print("-"*45)

menu()
