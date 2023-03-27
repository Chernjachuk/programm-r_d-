# dz 4
print("Enter the Text")
T_1 = input()
if T_1.isdigit():

    T_1 = int(T_1)
    if T_1 % 2 == 0:
        print("Chotnoe")


    else:
        print("nechotnoe")

else:
    print("v vashem tekste")
    print(len(T_1))
    print("simvolov")

# dop
print("Enter the Text")

T_1 = input()

match (T_1.isdigit()) == True:

    case True:
        print("Chisla")

    case _:
        print("tekst")