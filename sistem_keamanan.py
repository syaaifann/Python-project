# def registrasi_user ():
#     print("---FORM REGISTRASI---")
#     nama = input("masukan nama kamu: ")
#     levelAkses = input("masukan level akses kamu: ")
#     alamat = input("alamat kamu: ")
#     return nama, levelAkses, alamat
db_user = {
    1111 : {"nama" :"ipan", "level": "admin"},
    2222 : {"nama":"anon","level": "member"},
    3333 : {"nama": "ghostbyte", "level":"guest"}
    }
# def sistem_login (nama_pendaftar, level_pendaftar, alamat_pendaftar):
def sistem_login (database):
    print("\n---FORM LOGIN---")
    kesempatan = 3
    while kesempatan > 0:
        id = int(input("masukan id kamu: "))
        
        # if id in daftar_id_sah:
        #     print(f"[SYSTEM]: user '{nama_pendaftar}' dengan id {id} terdaftar sebagai {level_pendaftar}, alamat {alamat_pendaftar}, login sukses! saat ini ada {len(daftar_id_sah)} user di database:")
        #     break
        if id in database:
            nama_ditemukan = database[id]["nama"]
            level_ditemukan = database[id]["level"]
            print(f"""
[SYSTEM]: login berhasil 
nama : {nama_ditemukan} 
level : {level_ditemukan}
""")
            break
        else:
            kesempatan -= 1
            print(f"[PERINGATAN]: kesempatan kamu tinggal {kesempatan}")
            
            if kesempatan == 0:
                print(f"[PERINGATAN]: terlalu banyak percobaan, sistem anda terkunci")

# user_baru, level_baru, alamat_baru = registrasi_user()
# sistem_login(user_baru, level_baru, alamat_baru)

sistem_login(db_user)