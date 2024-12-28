import random

# Fungsi untuk membaca nama-nama depan dan belakang dari file NAME.TXT
def read_names_from_file(filename="NAME.TXT"):
    try:
        with open(filename, 'r') as file:
            # Membaca semua baris dari file dan memisahkan nama depan dan belakang
            names = [line.strip().split() for line in file.readlines()]
        return names
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan!")
        return []

# Fungsi untuk membuat pasangan nama secara acak dalam format nama:Nama1-1000
def generate_name_pairs(names, count=10):
    pairs = []
    for _ in range(count):
        first_name, last_name = random.choice(names)  # Pilih pasangan nama depan dan belakang secara acak
        number = random.randint(1, 1000)  # Pilih angka acak antara 1 hingga 1000
        
        # Pilih nama depan atau belakang secara acak untuk pasangan
        if random.choice([True, False]):  # Pilih True atau False secara acak
            pair = f"{first_name}:{first_name.capitalize()}{number}"  # Format namaDepan:namaDepan1-1000
        else:
            pair = f"{firts_name}:{lastname_name.capitalize()}{number}"  # Format namaBelakang:namaBelakang1-1000
            pair = f"{name}:{name.capitalize()}{number}"  # Format Format nama:Nama123
        
        pairs.append(pair)
    return pairs

# Fungsi untuk menyimpan pasangan nama ke dalam file .txt
def save_pairs_to_file(pairs, output_filename="generated_names.txt"):
    with open(output_filename, 'w') as f:
        for pair in pairs:
            f.write(pair + "\n")

# Membaca nama-nama dari file NAME.TXT
names = read_names_from_file("NAME.TXT")

# Jika nama ditemukan, buat pasangan nama secara acak dalam format nama:Nama1-1000
if names:
    # Generate 100 pasangan nama secara acak (atau sesuai kebutuhan)
    pairs = generate_name_pairs(names, count=100)

    # Simpan hasil pasangan nama ke dalam file .txt
    save_pairs_to_file(pairs, output_filename="generated_names.txt")

    print(f"Hasil telah disimpan di file 'generated_names.txt' dengan {len(pairs)} pasangan nama.")
else:
    print("Tidak ada nama yang ditemukan dalam file NAME.TXT.")
