#1 Básico : imprime todos los enteros del 0 al 150.
for i in range(151):
    print(i)
# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for i in range(5,1001,5):
    print(i)
# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. 
# Si es divisible por 10, imprima "Coding Dojo".
for i in range(1,100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final
sum = 0
for i in range(0,50000):
    if i % 2 != 0:
        sum+=i
print (sum)    
# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for i in range(2018,0,-4):
    print(i)
# Contador flexible : establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. 
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 2
higNum = 9
mult = 3
for i in range  (lowNum,(higNum+1)):
    if i % mult == 0:
        print(i)
# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000
def esPrimo (n): #Creo una función que detecta si un número es primo o no
    if n < 2:
        return False # Debe ser mayor a dos
    for i in range (2,n):
        if n%i == 0:
            return False # Si alguno de los restos de las divisiones entre el número y 
                            # cualquier número menor a este es 0, es porque no es primo 
                            # (p ej: 7/4 da un float de resultado, 8/4 da 0 de diferencia, por ende no es primo)
    else:
        return True # Si algún número es mayor a 0 y el resto de la división entre este número y cualquier otro menor no da 0
def sonPrimos (m):
    lista = []
    contador = 0
    i = 0
    while contador < m+1: # El contador llegará hasta el número que se ingrese a la función
        i += 1
        if esPrimo(i): # Si i da True para la función esPrimo, hace lo siguiente
            lista.append(i) # Añade este número a la lista 
        contador += 1 
    return lista
y = sonPrimos(1000)
print(y)
