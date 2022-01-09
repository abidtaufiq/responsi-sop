# Nama          : Abid Taufiqur Rohman
# NIM           : 5200411064
# Mata Kuliah   : Sistem Oprasi Praktik (V)
# Program Studi : Informatika

print ("=================================")
print ("|         MENEJEMEN RAM         |")
print ("=================================")
#inputan user
ram = int(input("Kapasitas RAM :"))
petabit = int(input("Total Petabit :"))
ramOs = int(input("Kapasitas Ram yang digunakan oleh sistem operasi :"))
ramstu = int(input("Kapasitas Ram yang digunakan oleh program 1 :"))
ramdua = int(input("Kapasitas Ram yang digunakan oleh program 2 :"))
#rumus perhitungan
#rumus total RAM
totalRam = ramOs + ramstu + ramdua
#rumus Ram yang tidak terpakai
ramTidak = ram - totalRam
#rumus kapasitas petabid
kapPetabit = totalRam-petabit
#rumus jumlah blok 1
blokstu = totalRam / kapPetabit
#rumus jumlah blok 0 
bloknol = kapPetabit-totalRam
#output yang ditampilkan
print ("----------------------------------------------")
print ("Total RAM                       =",ram)
print ("Total Petabit                   =",petabit)
print ("Kapasitas Per Petabit           =",kapPetabit)
print ("Total yang terpakai             =",totalRam)
print ("Total Ram yang tidak terpakai   =",ramTidak)
print ("Jumlah Blok yang bernilai 1     =",blokstu)
print ("Jumlah Blok yang bernilai 0     =",bloknol)

