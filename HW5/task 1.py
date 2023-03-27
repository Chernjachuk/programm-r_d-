print("vvedite text")
tekst = input()
print(tekst)
Simvoly = list(tekst)
kolychestvo_syvolov = len(tekst)

for simbol in tekst:
    if simbol.isalpha():
        if simbol.isupper():
            print(simbol)
            print("Velyki Litery")
        else:
            print(simbol)
            print("Malen'ky Litery")
    elif simbol.isdigit():
        if int(simbol) % 2 == 0:
            print(simbol)
            print("parni")
        else:
            print(simbol)
            print("neparni")
    else:

        print(simbol)
        print("ce znak")

print("Poka")