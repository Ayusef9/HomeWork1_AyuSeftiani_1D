# Menu Makanan Hari Ini
daftar_menu = {"Nasi Lauk" : 8000 , "Mie Ayam" : 12000 , "Soto Ayam" : 12000 , "Mie Goreng" : 10000}
print(daftar_menu)

# Pesan Makanan dan Minuman
nama = input('Masukan Nama :')
waktu_ambil = int(input('Ambil Pada Pukul :'))
nomer_oderan = int(input('No Orderan :'))
pesan_menu = input('Masukan Pesanan :')
total_biaya = int(input('Harga :'))
hasil = 'Anda Berhasil Memesan' if (pesan_menu in (daftar_menu)) else 'Tidak Berhasil' 
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








