nama = input("masukan nama kamu: ")
levelAkses = input("masukan level akses kamu: ")

kesempatan = 3
while kesempatan > 0:
    id = int(input("masukan id kamu: "))

    if id == 1111:
        print(f"[SYSTEM]: user '{nama}' dengan id {id} terdaftar sebagai {levelAkses}:")
        break
    else:
        kesempatan -= 1
        print(f"[PERINGATAN]: kesempatan kamu tinggal {kesempatan}")

        if kesempatan == 0:
            print(f"[PERINGATAN]: terlalu banyak percobaan, sistem anda terkunci")