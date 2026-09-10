devices = ["R1", "R2", "R3", "AP1", "AP2"]
koordinat = (-7.98, 112.63)
perangkat = {
    "dev1": { 
    "nama": "R1",
    "ip": "192.168.1.1",
    "status": "up"
},
    "dev2": { 
    "nama": "R2",
    "ip": "192.168.1.2",
    "status": "down"
},
    "dev3": { 
    "nama": "R3",
    "ip": "192.168.1.3",
    "status": "up"
},
    "dev4": { 
    "nama": "AP1",
    "ip": "192.168.1.4",
    "status": "up"
},
    "dev5": { 
    "nama": "AP2",
    "ip": "192.168.1.5",
    "status": "down" 
},
}
import json
print(json.dumps(perangkat, indent=4))