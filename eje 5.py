'''e. Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de
números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista
e imprima ambas. La lista de números la ingresa el usuario en forma de números
separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81'''
lista=[1,2,3,4,5,6,7,8,9]
def numero_par_impar(entrada):
    par=[]
    impar=[]
    for numero in entrada:
        if numero %2!=0:
            nuevo=numero**2
            impar.append(nuevo)
        else:
            par.append(numero)
    print(impar)
    print(par)

numero_par_impar(lista)