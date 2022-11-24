daftar = input("Masukan daftar pesanan : ")

pedagang= daftar.split()

print("Daftar pesanan : ",pedagang )

nambah= input("Masukan pesanan yang ingin ditambahkan: ")

pedagang.append(nambah)

print("Hasil penambahan dalam pesanan: ",pedagang)