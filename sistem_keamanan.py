nama = input("masukan nama kamu: ")
levelAkses = input("masukan level akses kamu: ")

kesempatan = 3
daftar_id_sah = [1111, 2222, 3333]
while kesempatan > 0:
    id = int(input("masukan id kamu: "))

    if id in daftar_id_sah:
        print(f"[SYSTEM]: user '{nama}' dengan id {id} terdaftar sebagai {levelAkses}, login sukses! saat ini ada {len(daftar_id_sah)} user di database:")
        break
    else:
        kesempatan -= 1
        print(f"[PERINGATAN]: kesempatan kamu tinggal {kesempatan}")

        if kesempatan == 0:
            print(f"[PERINGATAN]: terlalu banyak percobaan, sistem anda terkunci")