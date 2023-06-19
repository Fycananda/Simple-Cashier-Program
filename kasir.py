#--- DISKON YANG HARUS ADA ---
#50.000 - 75.000 = 15%dc
#80.000 - 115.000 = 20%dc
#350.000 = 25%dc

print("-------------------------SELAMAT DATANG DI PROGRAM KASIR-------------------------")

#--- PEMBAYARAN ---
Pembayaran_Pertama = int(input("Masukkan Nilai Pembayaran Pertama :Rp."))
Pembayaran_Kedua = int(input("Masukkan Nilai Pembayaran Kedua :Rp."))

#--- TOTAL PEMBAYARAN ---
Total_Pembayaran = int(Pembayaran_Pertama) + int(Pembayaran_Kedua) 

#--- DISKON YANG TERSEDIA ---
diskon_5075 = float(0.15)
diskon_80115 = float(0.20)
diskon_350 = float(0.25)

#--- PERHITUNGAN DISKON PERTAMA ---
total_diskon1 = int(Total_Pembayaran) * float(diskon_5075)
jumlah_total_harga1 = int(Total_Pembayaran) - int(total_diskon1)

#--- PERHITUNGAN DISKON KEDUA ---
total_diskon2 = int(Total_Pembayaran) * float(diskon_80115)
jumlah_total_harga2 = int(Total_Pembayaran) - int(total_diskon2)

#--- PERHITUNGAN DISKON KETIGA ---
total_diskon3 = int(Total_Pembayaran) * float(diskon_350)
jumlah_total_harga3 = int(Total_Pembayaran) - int(total_diskon3)

#--- STATEMENT PEMBERIAN DISKON ---
print("---------------------------------------------------------------------------------")

if Total_Pembayaran >=50_000 and Total_Pembayaran <=75_000:
    print("Selamat anda mendapakan diskon sebesar: 15%, atau setara dengan: " + "Rp." +  str(total_diskon1) + "0;")
    print(jumlah_total_harga1)
elif Total_Pembayaran <=79_999:
    print("Selamat anda mendapakan diskon sebesar: 15%, atau setara dengan: " + "Rp." +  str(total_diskon1) + "0;")
    print(jumlah_total_harga1)
elif Total_Pembayaran >=80_000 and Total_Pembayaran <=115_000:
    print("Selamat anda mendapakan diskon sebesar: 20%, atau setara dengan: " + "Rp." +  str(total_diskon2) + "0;")
    print(jumlah_total_harga2)
elif Total_Pembayaran <=349_999:
    print("Selamat anda mendapakan diskon sebesar: 20%, atau setara dengan: " + "Rp." +  str(total_diskon2) + "0;")
    print(jumlah_total_harga2)
elif Total_Pembayaran >=350_000:
    print("Selamat anda mendapakan diskon sebesar: 25%, atau setara dengan: " + "Rp." +  str(total_diskon3) + "0;")
    print(jumlah_total_harga3)
else:
    print("Maaf anda tidak mendapatkan Diskon")

print("-----------------------------------TERIMAKASIH-----------------------------------")