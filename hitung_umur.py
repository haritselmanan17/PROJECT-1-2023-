import datetime

print("Silahkan masukan tanggal,\nbulan dan tahun lahir anda \n")
tanggal = int (input("tanggal \t: "))
bulan = int (input("bulan \t\t: "))
tahun = int (input("tahun\t\t: "))

tanggal_lahir = datetime.date(tahun,bulan,tanggal)
print(f"Tanggal Lahir Anda Adalah: {tanggal_lahir}")


hari_ini = datetime.date.today()
print(f"Hari Ini Tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days //365
umur_bulan_sisa = (umur_hari.days % 365) //30

print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
