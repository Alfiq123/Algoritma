def cmyk_to_rgb(c, m, y, k):
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    return int(r), int(g), int(b)

def rgb_to_cmyk(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0
    k = 1 - max(r, g, b)
    if k == 1:
        return 0, 0, 0, 1
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return int(c * 100), int(m * 100), int(y * 100), int(k * 100)

while True:
    print("Pilih konversi:")
    print("1. CMYK ke RGB")
    print("2. RGB ke CMYK")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        c = float(input("Masukkan nilai C (0-100): "))
        m = float(input("Masukkan nilai M (0-100): "))
        y = float(input("Masukkan nilai Y (0-100): "))
        k = float(input("Masukkan nilai K (0-100): "))
        if 0 <= c <= 100 and 0 <= m <= 100 and 0 <= y <= 100 and 0 <= k <= 100:
            r, g, b = cmyk_to_rgb(c / 100, m / 100, y / 100, k / 100)
            print(f"Nilai RGB: ({r}, {g}, {b})")