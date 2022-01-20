
resultado = 0
numero = int(input("Ingrese un numero: "))

for i in range(1, 4):
    resultado += numero**i

print("El resultado de la operacion de n + n*n + n*n*n: ", resultado)