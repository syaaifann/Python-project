def registrasi_user ():
    print("---FORM REGISTRASI---")
    nama = input("masukan nama kamu: ")
    levelAkses = input("masukan level akses kamu: ")
    alamat = input("alamat kamu: ")
    return nama, levelAkses, alamat

def sistem_login (nama_pendaftar, level_pendaftar, alamat_pendaftar):
    print("/n---FORM LOGIN---")
    kesempatan = 3
    daftar_id_sah = [1111, 2222, 3333]
    while kesempatan > 0:
        id = int(input("masukan id kamu: "))
        
        if id in daftar_id_sah:
            print(f"[SYSTEM]: user '{nama_pendaftar}' dengan id {id} terdaftar sebagai {level_pendaftar}, alamat {alamat_pendaftar}, login sukses! saat ini ada {len(daftar_id_sah)} user di database:")
            break
        else:
            kesempatan -= 1
            print(f"[PERINGATAN]: kesempatan kamu tinggal {kesempatan}")
            
            if kesempatan == 0:
                print(f"[PERINGATAN]: terlalu banyak percobaan, sistem anda terkunci")

user_baru, level_baru, alamat_baru = registrasi_user()
sistem_login(user_baru, level_baru, alamat_baru)