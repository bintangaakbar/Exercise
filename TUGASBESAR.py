import os
from time import sleep


loop = True


while loop:
    def menu():
        print("="*10)
        print("Pesan Rental Mobil")
        print("="*10)
        print("pilih kelas mobil! ")
        print("-"*10)
        print("1.   Luxury")
        print("2.   Sedan")
        print("3.   EXIT")
        print("-"*10)
    
    def pesan():
        jmlh = int(input("Mau sewa berapa hari ?   : "))
        num_array= list()
        org = input("berapa Penumpang di dalam mobil ?    : ")
        print("Masukkan nama penumpang  : ")
        for i in range (int(org)):
            i += 1
            n = input("Penumpang ke {}  : ".format(i))
            num_array.append(str(n))
        total_hrg = jmlh * harga
        os.system('cls')
        print("-"*10)
        print("Mobil",tipe, "telah dipesan!")
        print("Nama Penumpang   : ".format(len(num_array)))
        for a in num_array:
            print (("- {}").format(a))
        print("Total Harga", "Rp", total_hrg)
    
    menu()
    tipe = int(input("Pilih Tipe mobil  :   "))
    
    if ((tipe) == 1):
        print("-"*15)
        print("\nKode    Nama\tKelas\t   Harga /Hari")
        print("-"*15)
        print("\n101.   Camry\tLuxury \tRp. 900,000")
        print("\n102.   Alphard\tLuxury  \tRp. 1.500,000")
        print("\n103.   Accord\tLuxury \tRp. 800,000")
        print("-"*20)
        no_mobil = int(input("Masukkan kode mobil   :   "))

        if ((no_mobil) == 101):
            harga = 900000
            print("")
            print("-"*10)
            print("Anda telah memilih kode Mobil", int(no_mobil))
            print("-"*10)
            pesan()
        
        elif ((no_mobil) == 102):
            harga = 1500000
            print("")
            print("-"*10)
            print("Anda telah memilih kode Mobil", int(no_mobil))
            print("-"*10)
            pesan()

        elif ((no_mobil) == 103):
            harga = 800000
            print("")
            print("-"*10)
            print("Anda telah memilih kode Mobil", int(no_mobil))
            print("-"*10)
            pesan()
        
        else:
            os.system('cls')
            print("Yahh mobil itu tidak ada di rentalan kami, semoga kedepan nya ada yaa!")

    elif((tipe) == 2):
        print("-"*10)
        print("\nKode    Nama\tKelas\tHarga /Hari")
        print("-"*10)
        print("\n201.   Civic\tSedan\tRp. 1.100,000")
        print("\n202.   BMW I8\tSedan\tRp. 1.500,000")
        print("\n203.   Vios\tSedan\tRp. 800,000")
        print("-"*20)
        no_mobil = int(input("Masukkan kode Mobil   :   "))

        if ((no_mobil) == 201):
            harga = 1100000
            print("")
            print("-"*10)
            print("Anda telah memilih kode Mobil", int(no_mobil))
            print("-"*10)
            pesan()
        
        elif ((no_mobil) == 202):
            harga = 1500000
            print("")
            print("-"*10)
            print("Anda telah memilih kode Mobil", int(no_mobil))
            print("-"*10)
            pesan()

        elif ((no_mobil) == 203):
            harga = 800000
            print("")
            print("-"*10)
            print("Anda telah memilih kode Mobil", int(no_mobil))
            print("-"*10)
            pesan()
        
        else:
            os.system('cls')
            print("Yahh mobil itu tidak ada di rentalan kami, semoga kedepan nya ada yaa!")

    elif ((tipe) == 3):
         print("")
         print("\t  >>> Sampai Jumpa lagi <<<")
         sleep(2)
         os.system('cls')
         sleep(1)
         exit
         sleep(1)
