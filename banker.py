# banker.py - Simulasi algoritma Banker untuk K-3 (Kelompok 4, Kelas D)
# Kasus: checkout toko online. R1 = lock tabel stok, R2 = lock transaksi
# pembayaran, R3 = slot kurir.
# CATATAN: matriks di bawah adalah DATA CONTOH. Ganti dengan matriks kelas.

P = ["C1", "C2", "C3", "C4", "C5"]
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
mx    = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
avail = [3, 3, 2]
M = len(avail)


def hitung_need(a, m):
    return [[m[i][j] - a[i][j] for j in range(M)] for i in range(len(a))]


def aman(a, m, av):
    need = hitung_need(a, m)
    work, selesai, urut = av[:], [False] * len(a), []
    while True:
        for i in range(len(a)):
            if not selesai[i] and all(need[i][j] <= work[j] for j in range(M)):
                work = [work[j] + a[i][j] for j in range(M)]
                selesai[i] = True
                urut.append(P[i])
                print(f"  pilih {P[i]}: Work -> {work}")
                break
        else:
            break
    return all(selesai), urut


def minta(i, req, a, m, av):
    need = hitung_need(a, m)
    if any(req[j] > need[i][j] for j in range(M)):
        return "DITOLAK: melebihi Need"
    if any(req[j] > av[j] for j in range(M)):
        return "MENUNGGU: melebihi Available"
    a2 = [r[:] for r in a]
    av2 = av[:]
    for j in range(M):
        av2[j] -= req[j]
        a2[i][j] += req[j]
    ok, urut = aman(a2, m, av2)
    return ("DIKABULKAN, urutan " + str(urut)) if ok else "DITUNDA: unsafe"


print("Need:", hitung_need(alloc, mx))
ok, urut = aman(alloc, mx, avail)
print("Keadaan awal:", "SAFE" if ok else "UNSAFE", urut)
print("C2 minta (1,0,2):", minta(1, [1, 0, 2], alloc, mx, avail))
print("C5 minta (3,3,0):", minta(4, [3, 3, 0], alloc, mx, avail))
print("C1 minta (0,0,4):", minta(0, [0, 0, 4], alloc, mx, avail))
print("C3 minta (4,0,0):", minta(2, [4, 0, 0], alloc, mx, avail))
