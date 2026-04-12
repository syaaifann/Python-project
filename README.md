# Python-project🔗

## Code xample 1

```
nama = input("masukan nama kamu: ")
id = int(input("masukan id kamu: "))
levelAkses = input("masukan level akses kamu: ")

print(f"[SYSTEM]: user '{nama}' dengan id {id} telah terdaftar sebagai {levelAkses}.")

```

---

## Code xample 2

### penambahan logika if else

```
nama = input("masukan nama kamu: ")
id = int(input("masukan id kamu: "))
levelAkses = input("masukan level akses kamu: ")

if id == 1111:
    print(f"[SYSTEM]: user '{nama}' dengan id {id} telah terdaftar sebagai {levelAkses}.")

else :
    print(f"[PERINGATAN]: id {id} tidak dikenal, akses diblokir")

```

---

## Code xample 3

### meningkatkan sistem anti brute force

```
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

```

---

## Code xample 4

## Menambahkan Daftar id sah

```
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

```
