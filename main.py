# Menu Makanan dan Minuman Hari Ini
daftar_menu = {"Nasi Lauk" : 8000 , "Mie Ayam" : 12000 , "Soto Ayam" : 12000 , "Mie Goreng" : 10000}
minuman = {"Es Teh" : 5000 , "Air Putih" : 3000}
print(daftar_menu)
print(minuman)
# Pesan Makanan dan Minuman
nama = input('Masukan Nama :')
waktu_ambil = int(input('Ambil Pada Pukul :'))
nomer_oderan = int(input('No Orderan :'))
pesan_menu = (daftar_menu['Soto Ayam'] , (minuman['Es Teh']))
total_biaya = 12000 + 5000
hasil = 'Anda Berhasil Memesan' if ('Soto Ayam' in (daftar_menu) and 'Es Teh' in (minuman)) else 'Tidak Berhasil'
print(pesan_menu)
print(hasil)
print(total_biaya)
# Pembayaran
non_tunai = True
tunai = False
hasil = ' Anda Berhasil Membayar' if (non_tunai == True) else ' Anda Tidak Berhasil Membayar'
print(hasil)
ucapan = "Terima Kasih Sudah Memesan , Semoga Hari Anda Menyenangkan"
print(ucapan)








