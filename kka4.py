perangkat_jaringan = {
    "dev1": {"nama": "R1", "ip": "192.168.1.1", "status": "up"},
    "dev2": {"nama": "R2", "ip": "192.168.1.2", "status": "down"},
    "dev3": {"nama": "R3", "ip": "192.168.1.3", "status": "up"},
    "dev4": {"nama": "AP1", "ip": "192.168.1.4", "status": "up"},
    "dev5": {"nama": "AP2", "ip": "192.168.1.5", "status": "down"}
}

for data in perangkat_jaringan.values():
    print(f"Nama: {data['nama']} | IP: {data['ip']} | Status: {data['status']}")
def cek_status(nama, status):
    if status == "up":
        return f"{nama} aktif"
    else:
        return f"{nama} mati"

def hitung_ringkasan(data):
    aktif = 0
    tidak_aktif = 0
    for dev in data.values():
        if dev["status"] == "up":
            aktif += 1
        else:
            tidak_aktif += 1
    return aktif, tidak_aktif

print("=" * 45)
print("    SISTEM MONITORING JARINGAN")
print("=" * 45)

print("\n--- STATUS DETAIL PERANGKAT ---")
for dev in perangkat_jaringan.values():
    print(f"- IP: {dev['ip']:<13} | {cek_status(dev['nama'], dev['status'])}")

jumlah_aktif, jumlah_tidak_aktif = hitung_ringkasan(perangkat_jaringan)

print("--- RINGKASAN STATUS PERANGKAT ---")
print(f"Perangkat Aktif (up)        : {jumlah_aktif} unit")
print(f"Perangkat Tidak Aktif (down)  : {jumlah_tidak_aktif} unit")
print(f"Total Perangkat             : {jumlah_aktif + jumlah_tidak_aktif} unit")
print("=" * 45)