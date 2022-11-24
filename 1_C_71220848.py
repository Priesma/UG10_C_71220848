print("========== Pilih menu ==========")
print(' 1. Jumlah ')
print(' 2. Kurang ')
print(' 3. Kali ')
print(' 4. Bagi ')

angka_1 = eval(input('Masukkan bilangan pertama: '))
angka_2 = eval(input('Masukkan bilangan kedua: '))

operasi = input('Pilih Anda: ')

if operasi == '1':
  hasil = angka_1 + angka_2
  print(f'Hasil: {hasil}')
elif operasi == '2':
  hasil = angka_1 - angka_2
  print(f'Hasil: {hasil}')
elif operasi == '3':
  hasil = angka_1 * angka_2
  print(f'Hasil: {hasil}')
elif operasi == '4':
  hasil = angka_1 / angka_2
  print(f'Hasil: {hasil}')