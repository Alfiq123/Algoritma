import math

# Panjang diameter suatu lingkaran jika diketahui LUAS-nya

# luas = int(input("Masukkan luas dari lingkaran: "))

print("🟢 ===== Mencari panjang diameter suatu lingkaran jika diketahui LUAS-nya ===== 🟢")

# Input di dalam pengulangan.
while True:
    try:
        # Menerima Integer dan Float.
        luas = int(float(input("Masukkan luas dari lingkaran: ")))
    # Error jika memasukkan huruf.
    except ValueError:
        print("⛔️ Kamu tidak memasukkan angka ⛔️")
        continue
    else:
        break

# Rumus = 2 * √(luas / π).
diameter = 2 * math.sqrt(luas / math.pi)

# Hasil.
print("🏆 ===== Hasilnya adalah: ===== 🏆")
print(f"Diameter lingkaran tersebut adalah: {diameter:.2f} cm")

# Diperbarui dengan - Stacloverflow
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
