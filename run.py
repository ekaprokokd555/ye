import random

# Fungsi untuk membaca nama-nama dari file NAME.TXT
def read_names_from_file(filename="NAME.TXT"):
    try:
        with open(filename, 'r') as file:
            # Membaca semua baris dari file dan menghapus karakter spasi ekstra
            names = [line.strip() for line in file.readlines()]
        return names
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan!")
        return []

# Fungsi untuk membuat pasangan nama:nama123 secara acak
def generate_name_pairs(names, count=10):
    pairs = []
    for _ in range(count):
        name = random.choice(names)  # Pilih nama secara acak
        pair = f"{name}:{name.lower()}123"  # Format nama:nama123
        pairs.append(pair)
    return pairs

# Fungsi untuk menyimpan pasangan nama:nama123 ke dalam file .txt
def save_pairs_to_file(pairs, output_filename="generated_names.txt"):
    with open(output_filename, 'w') as f:
        for pair in pairs:
            f.write(pair + "\n")

# Membaca nama-nama dari file NAME.TXT
names = read_names_from_file("NAME.TXT")

# Jika nama ditemukan, buat pasangan nama:nama123
if names:
    # Generate 100 pasangan nama:nama123 secara acak (atau sesuai kebutuhan)
    pairs = generate_name_pairs(names, count=100)

    # Simpan hasil pasangan nama:nama123 ke dalam file .txt
    save_pairs_to_file(pairs, output_filename="generated_names.txt")

    print(f"Hasil telah disimpan di file 'generated_names.txt' dengan {len(pairs)} pasangan nama.")
else:
    print("Tidak ada nama yang ditemukan dalam file NAME.TXT.")
