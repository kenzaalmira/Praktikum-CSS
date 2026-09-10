nama = "kenza"
umur = 17

print ("Nama:", nama)
print("Umur:", umur)
print(umur > 17)

status = "up"

if status == "up":
    print("Perangkat Aktif")
elif status == "down":
    print("Perangkat Mati")
else: 
    print("Status Tidak Diketahui")

devices = ["R1", "R2", "R3", "R4", "R5"]
for d in devices:
    print(d, "dicek...")

bandwidth = 0 
while bandwidth < 100:
    bandwidth += 20
    print(bandwidth)

batas = 80
pemakaian = [40, 95, 65, 70, 82]

for nilai in pemakaian:
    if nilai > batas:
        print(nilai, "-> PERINGATAN")
    else:
        print(nilai, "-> normal")
