import os
from time import sleep

loop = True

while loop:
    def menu():
        print("="*10)
        print("Pesan Lapangan Futsal")
        print("="*10)
        print("pilih Tipe Lapangan! ")
        print("-"*10)
        print("1.   Karpet")
        print("2.   Rumput")
        print("3.   Semen")
        print("4.   EXIT")
        print("-"*10)

    def pesan():
        jmlh = int(input("Mau main berapa jam ?   : "))
        num_array= list()
        org = input("Pesanan atas nama  :  ")
        total_hrg = jmlh * harga
        os.system('cls')
        print("-"*10)
        print("Lapangan telah dipesan!")
        print("Atas nama   : ", org.format(len(num_array)))
        for a in num_array:
            print (("- {}").format(a))
        print("Total Harga", "Rp", total_hrg)
    
    menu()
    tipe = int(input("Pilih Tipe Lapangan  :   "))

    if ((tipe) == 1):
        print("-"*15)
        print("\nNomor    Nama\tTipe\t   Harga per Jam")
        print("-"*15)
        print("\n101.   Damar\tKarpet \tRp. 150,000")
        print("\n102.   Bangkit\tKarpet \tRp. 150,000")
        print("-"*20)
        no_lpg = int(input("Masukkan No lapangan   :   "))

        if ((no_lpg) == 101):
            harga = 150000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        elif ((no_lpg) == 102):
            harga = 150000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        else:
            print("\t   Yahh lapangan Belum tersedia di tempat kami, semoga kedepan nya ada yaa!")
            sleep(3)
            os.system('cls')

    elif((tipe) == 2):
        print("-"*10)
        print("\nNomor    Nama\tTipe\tHarga per Jam")
        print("-"*10)
        print("\n201.   Karang\tRumput\tRp. 100,000")
        print("\n202.   Mangudu\tRumput\tRp. 100,000")
        print("-"*20)

        no_lpg = int(input("Masukkan Nomor Lapangan   :   "))

        if ((no_lpg) == 201):
            harga = 100000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        elif ((no_lpg) == 202):
            harga = 100000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()
        
        else:
            print("\t   Yahh lapangan Belum tersedia di tempat kami, semoga kedepan nya ada yaa!")
            sleep(3)
            os.system('cls')

    elif((tipe) == 3):
        print("-"*10)
        print("\nNomor    Nama\tTipe\tHarga per Jam")
        print("-"*10)
        print("\n301.   Barung\tSemen\tRp. 80,000")
        print("\n302.   Deli\tSemen\tRp. 80,000")
        print("-"*20)
        no_lpg = int(input("Masukkan Nomor Lapangan   :   "))

        if ((no_lpg) == 301):
            harga = 80000
            print("")
            print("-"*10)
            print("Anda telah memilih Lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        elif ((no_lpg) == 302):
            harga = 80000
            print("")
            print("-"*10)
            print("Anda telah memilih Lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        else:
            print("\t   Yahh lapangan Belum tersedia di tempat kami, semoga kedepan nya ada yaa!")
            sleep(3)
            os.system('cls')      

    elif ((tipe) == 4):
        print("")
        print("\t  >>> Sampai Jumpa lagi <<<")
        sleep(2)
        os.system('cls')
        sleep(1)
        exit
        sleep(1)

    else:
        os.system('cls')
        print(">>>  Maaf, Lapangan tidak ada di list kami!   <<<")