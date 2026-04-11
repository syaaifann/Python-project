nama = input("masukan nama kamu: ")
id = int(input("masukan id kamu: "))
levelAkses = input("masukan level akses kamu: ")

if id == 1111:
    print(f"[SYSTEM]: user '{nama}' dengan id {id} telah terdaftar sebagai {levelAkses}.")

else :
    print(f"[PERINGATAN]: id {id} tidak dikenal, akses diblokir")