# Nama          : Abid Taufiqur Rohman
# NIM           : 5200411064
# Mata Kuliah   : Sistem Oprasi Praktik (V)
# Program Studi : Informatika

#Oprasi
def createQueue():
    dataQueue = []
    return dataQueue
def enqueue(dataQueue,data):
    dataQueue.insert(0,data)
    return dataQueue
def dequeue(dataQueue):
    data = dataQueue.pop()
    return data
def isEmpty(dataQueue):
    return dataQueue==[]
def size(dataQueue):
    return len(dataQueue)

#fungsi Input data
def inputdata(jumlah):
    tampung = []
    for i in range (jumlah):
        nama = input("Nama Program ke-{} : " .format(i)).upper()
        waktu = int(input("Lama proses waktu pengerjaan : "))
        tampung.append([nama,waktu])
    return tampung

#fungsi task schedulling untuk mengatur jadwal
def Task_Schedulling(waktu_Prosesor,tugas):
    q = createQueue()
    for i in tugas:
        enqueue(q,i)
    print ("Jadwal antrian tugas",q)
    hitung = 1
    while not isEmpty(q):
        print ("Iterasi ke-",hitung)
        hitung += 1
        #menghapus data dari antrian
        temp = dequeue(q)
        #oprasi pengurangan, jika lebih besar dari 0 akan diproses lagi
        pengurangan = temp[1] - waktu_Prosesor
        if pengurangan > 0:
            enqueue(q,temp)
            q [0][1] = pengurangan
            print ("\tProgram {} sedang di proses, sisa waktu proses {} = {}".format(temp[0],temp[0],pengurangan))
        else:
            print ("\tProgram {} telah selesai diproses".format(temp[0]))

        print ("\tData proses yang tersisa",q)

jumlah = int(input("Jumlah pemrosesan yang akan di jadwalkan : "))
task = inputdata(jumlah)
waktu = int(input("Jatah waktu (Quantum Time) : "))
print ("----------------------------------------------------")
print ("Jatah waktu (Quantum Time) :",waktu)

Task_Schedulling(waktu,task)