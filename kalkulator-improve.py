# aplikasi kalkulator yang mensupport (+, -, x, /, exit)
# tetapi saya ingin improve program ini supaya operasinya lebih kompleks
command = ""

while command != "exit":
    command = input("Perintah : ")
    
    if command == "exit":
        break #perintah break disebut sebagai flow control / kontrol aliran. break ini digunakan untuk menghentikan loop secara langsung.
    
    if command != "+" and command != "-" and command != "*" and command != "/" and command != "**" and command != "%":
        print("Perintah tidak dikenali")
        continue #perintah continue ini disebut sebagai flow control / kontrol aliran. continue ini digunakan untuk melanjutkan ke iterasi berikutnya dalam perulangan atau loop.
    
    if command == "+":
        print("Penjumlahan")
        a = int(input("Angka pertama : "))
        b = int(input("Angka kedua : "))
        result = a + b
    elif command == "-":
        print("Pengurangan")
        a = int(input("Angka pertama : "))
        b = int(input("Angka kedua : "))
        result = a - b
    elif command == "*":
        print("Perkalian")
        a = int(input("Angka pertama : "))
        b = int(input("Angka kedua : "))
        result = a * b
    elif command == "/":
        print("Pembagian")
        a = int(input("Angka pertama : "))
        b = int(input("Angka kedua : "))
        result = a / b
    elif command == "**":
        print("Perpangkatan")
        a = int(input("Angka pertama : "))
        b = int(input("Angka kedua : "))
        result = a ** b
    elif command == "%":
        print("Modulus")
        a = int(input("Angka pertama : "))
        b = int(input("Angka kedua : "))
        result = a % b
    
    print(f"Hasil : {result} ")
    
print("Terima kasih sudah menggunakan aplikasi kami")