# 1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing
data_panen = {  
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

for key, value in data_panen.items():
    print(f"Hasil panen {value['nama_lokasi']}:")
    print(f"Padi: {value['hasil_panen']['padi']}")
    print(f"Jagung: {value['hasil_panen']['jagung']}")
    print(f"Kedelai: {value['hasil_panen']['kedelai']}\n")


# 2. Tampilkan jumlah hasil panen jagung dari lokasi-lokasi
jumlah_jagung = sum(value['hasil_panen']['jagung'] for value in data_panen.values())
print(f"Jumlah hasil panen jagung dari semua lokasi: {jumlah_jagung}")

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")

# 4. Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda

data_panen = {  
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

jumlah_padi = []
jumlah_kedelai = []


for lokasi in data_panen.values():
    hasil = lokasi['hasil_panen']
    jumlah_padi.append(hasil['padi'])
    jumlah_kedelai.append(hasil['kedelai'])


print("Jumlah Hasil Panen Padi:", jumlah_padi)
print("Jumlah Hasil Panen Kedelai:", jumlah_kedelai)


# 5. Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.

data_panen = {  
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']

kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']


print("Hasil Panen Padi:")
print(f"Kebun A: {padi_lokasi1}")
print(f"Kebun B: {padi_lokasi2}")
print(f"Kebun C: {padi_lokasi3}")
print(f"Kebun D: {padi_lokasi4}")
print(f"Kebun E: {padi_lokasi5}")

print("\nHasil Panen Kedelai:")
print(f"Kebun A: {kedelai_lokasi1}")
print(f"Kebun B: {kedelai_lokasi2}")
print(f"Kebun C: {kedelai_lokasi3}")
print(f"Kebun D: {kedelai_lokasi4}")
print(f"Kebun E: {kedelai_lokasi5}")

# 6 Buat Percabangan
# Jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus.
# Jika tidak, maka lokasi tersebut dalam kondisi baik.

data_panen = {  
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

for lokasi in data_panen.values():
    nama_lokasi = lokasi['nama_lokasi']
    hasil_panen = lokasi['hasil_panen']
    padi = hasil_panen['padi']
    jagung = hasil_panen['jagung']
    

    if padi > 1300 or jagung > 800:
        kondisi = "memerlukan perhatian khusus"
    else:
        kondisi = "dalam kondisi baik"
    
    print(f"{nama_lokasi}: {kondisi}")

print ('Tambah Branch Baru')