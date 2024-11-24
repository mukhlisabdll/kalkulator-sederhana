# Fungsi operasi matematika dasar
def tambah(angka1 , angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Error! Pembagian dengan 0 tidak diperbolehkan"

# Fungsi untuk menjalankan kalkulator
def kalkulator():
    ulangi = "y" # Variabel untuk menyimpan pilihan pengguna

    while ulangi.lower() == "y": # Selama pengguna memilih 'y', kalkulasi akan berulang
        print("\n--- Kalkulator Sederhana ---\n")
        print("Pilihan operasi:")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        
        # Mengambil input pilihan operasi 
        pilihan = input("Masukan pilihan (1/2/3/4): ")

        if pilihan in ["1", "2", "3", "4"]: # Jika pilihan valid
            angka1 = float(input("Masukan angka pertama: "))
            angka2 = float(input("Masukan angka kedua: "))

            # Menjalankan operasi sesuai pilihan
            if pilihan == '1':
                print("Hasil: ", tambah(angka1, angka2))
            elif pilihan == '2':
                print("Hasil:", kurang(angka1, angka2))
            elif pilihan == '3':
                print("Hasil:", kali(angka1, angka2))
            elif pilihan == '4':
                print("Hasil:", bagi(angka1, angka2))
        
        else:
            print("Pilihan tidak valid, coba lagi.")
        
        # Menanyakan apakah pengguna ingin melakukan kalkulasi lagi
        ulangi = input("Ingin mengulangi kalkulasi lagi? (y/n): ")

    print("Terima kasih telah menggunakan kalkulator!")

# Memanggil fungsi kalkulator
kalkulator()