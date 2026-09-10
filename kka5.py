devices = ["Router A", "Router B", "Router c", "Router D", "Router E"]
koordinat = (-7.250445, 112.768845)
print("Device pertama : ", devices[0])
print("Device pertama : ", devices[4])
print("Koordinat : ", koordinat)

perangkat_network = {
    "dev1": {"nama": "Router_A", "ip": "192.168.1.1", "status": "up"},
    "dev2": {"nama": "Switch_Core", "ip": "192.168.1.2", "status": "up"},
    "dev3": {"nama": "Firewall_01", "ip": "192.168.1.254", "status": "down"},
    "dev4": {"nama": "AccessPoint_1", "ip": "192.168.1.50", "status": "up"}
}
for id_perangkat, detail in perangkat_network.items():
    print(f"ID: {id_perangkat} | Nama: {detail['nama']} | IP: {detail['ip']} | Status: {detail['status']}")

def cek_status(nama, status):
    return f"Perangkat {nama} saat ini berstatus: {status.upper()}"
print(cek_status("Router_A", "down"))
print(cek_status("Router_B", "up"))
print(cek_status("Router_c", "up"))

def cek_semua(data):
    print("---Status Seluruh Perangkat---")
    for id_perangkat, detail in data.items():
        print(f"--{detail['nama']} ({detail['ip']}): Status = {detail['status']}")
def hitung_aktif(data):
    jumlah_aktif = 0
    for detail in data.values():
        if detail['status'].lower() == 'up':
            jumlah_aktif += 1
        return jumlah_aktif
cek_semua(perangkat_network)
total_up = hitung_aktif(perangkat_network)
print(f"\nTotal perangkat berstatus 'up': {total_up}")