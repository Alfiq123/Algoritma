# Panjang rusuk sebuah kubus jika diketahui VOLUME-nya.

# Input
# volume = int(input("Masukkan volume kubus: "))

print("🧊 ===== Mencari panjang rusuk kubus jika diketahui VOLUME-nya ===== 🧊")

# Input - Volume kubus
while True:
    try:
        volume = float(input("Masukkan volume kubus: "))
    except ValueError:
        print("🚩 Kamu memasukkan huruf atau karakter lain 🚩")
        continue
    else:
        break

# Rumus - s = ∛V
rusuk = volume  ** (1 / 3)

# Output
print("🏁 ===== Hasil ===== 🏁")
print(f"Volume kubus: {volume:.2f} cm³")
print(f"Rumus: ∛{volume:.2f} cm³")
print(f"Panjang rusuk kubus adalah: {rusuk:.2f} cm")
