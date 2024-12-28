import requests
from bs4 import BeautifulSoup
import random

# Fungsi untuk mengambil nama-nama dari halaman web
def get_names_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Daftar untuk menyimpan nama-nama yang diambil
    names = []
    
    # Mencari semua elemen yang berisi nama (asumsi nama berada dalam <td> dengan class tertentu)
    # Sesuaikan dengan elemen yang benar berdasarkan struktur halaman
    table_rows = soup.find_all('tr')  # Mencari seluruh baris tabel
    
    for row in table_rows:
        # Cari kolom yang berisi nama (misalnya pada kolom tertentu)
        cols = row.find_all('td')
        if len(cols) > 0:  # Memastikan ada data dalam baris
            name = cols[0].get_text().strip()  # Ambil teks dari kolom pertama
            if name:  # Pastikan nama tidak kosong
                names.append(name)
    
    return names

# Fungsi untuk membuat pasangan nama:nama123 secara acak
def generate_name_pairs(names, count=10):
    pairs = []
    for _ in range(count):
        name = random.choice(names)  # Pilih nama secara acak
        pair = f"{name}:{name.lower()}123"  # Format nama:nama123
        pairs.append(pair)
    
    return pairs

# Fungsi untuk menyimpan pasangan nama:nama123 ke file .txt
def save_pairs_to_file(pairs, filename="nama_pairs.txt"):
    with open(filename, 'w') as f:
        for pair in pairs:
            f.write(pair + "\n")

# URL dari halaman web yang berisi tabel dengan nama-nama
url = 'https://pddikti.kemdiktisaintek.go.id/search/bina%20nusantara?'

# Ambil nama-nama dari website
names = get_names_from_url(url)

# Jika nama ditemukan, buat pasangan nama:nama123
if names:
    # Generate 100 pasangan nama:nama123 secara acak (atau sesuai kebutuhan)
    pairs = generate_name_pairs(names, count=100)

    # Simpan hasil pasangan nama:nama123 ke dalam file .txt
    save_pairs_to_file(pairs, filename="nama_pairs.txt")

    print(f"Hasil telah disimpan di file 'nama_pairs.txt' dengan {len(pairs)} pasangan nama.")
else:
    print("Tidak ada nama yang ditemukan di halaman.")
