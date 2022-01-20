total = 0

print("Ingrese 5 numeros decimales\n")

while(total != 5):
    num = float(input("Ingrese un numero: "))
    if num%1 != 0:
        total+=1
    else:
        print("El numero ingresado no es decimal")
