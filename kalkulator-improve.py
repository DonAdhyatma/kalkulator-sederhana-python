# aplikasi kalkulator yang mensupport (+, -, x, /, exit)
# tetapi saya ingin improve program ini supaya operasinya lebih kompleks
command = ""

while command != "exit":
    command = input("Perintah : ")
    
    if command == "exit":
        break
    
    if command not in ["+", "-", "*", "/", "**", "%"]:
        print("Perintah tidak dikenali")
        continue

    if command == "+":
        print("Penjumlahan")
        try:
            a = int(input("Angka pertama : "))
            b = int(input("Angka kedua : "))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
        result = a + b
    elif command == "-":
        print("Pengurangan")
        try:
            a = int(input("Angka pertama : "))
            b = int(input("Angka kedua : "))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
        result = a - b
    elif command == "*":
        print("Perkalian")
        try:
            a = int(input("Angka pertama : "))
            b = int(input("Angka kedua : "))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
        result = a * b
    elif command == "/":
        print("Pembagian")
        try:
            a = int(input("Angka pertama : "))
            b = int(input("Angka kedua : "))
            result = a / b
        except ZeroDivisionError:
            print("Penyebut tidak boleh angka nol. Silakan coba lagi.")
            continue
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
    elif command == "**":
        print("Perpangkatan")
        try:
            a = int(input("Angka pertama : "))
            b = int(input("Angka kedua : "))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
        result = a ** b
    elif command == "%":
        print("Modulus")
        try:
            a = int(input("Angka pertama : "))
            b = int(input("Angka kedua : "))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
        result = a % b
    
    print(f"Hasil : {result} ")
    
print("Terima kasih sudah menggunakan aplikasi kami")