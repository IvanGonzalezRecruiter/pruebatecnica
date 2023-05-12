def primo (numero):
    if numero < 2:
        return False 
    for i in range (2,numero):
        if numero % i==0:
            return False
    return True

numero=int(input("Introduce un número entero positivo: "))
if primo(numero):
    print(f"{numero} es un numero primo")
else:
    print(f"{numero} NO es un numero primo")
