#PUEDE ENCONTRAR EL CASO FINAL EN GITHUB Y COLAB:
#https://github.com/dnnygmez11/DataScience/tree/main/Caso%20Final
#https://colab.research.google.com/drive/1zzfLjha3flmYQB1tFuv72REAkloE-RiN?usp=sharing

#EJERCICIO 8 MODULO 1
def es_num_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def producto_digitos(n):
    producto = 1
    while n > 0:
        ultimo_digito = n % 10  #obtiene eltimo dígito
        producto = producto * ultimo_digito 
        n = n // 10  #elimina el ultimo digito
    return producto

#da vuelta a los digitos
def espejo(n):
    numero_espejo = 0
    while n > 0:
        ultimo_digito = n % 10 
        numero_espejo = numero_espejo * 10 + ultimo_digito #se da vuelta a los digitos
        n = n // 10
    return numero_espejo
 
#Verifica si es el numero sheldon
def es_numero_sheldon(num, primos, posicion_primo):

    if not es_num_primo(num):
        print(f"{num} no es primo, no cumple la conjetura de Sheldon")
        return False
    else:
        print(f"{num} es primo")



    producto = producto_digitos(num)
    if producto != posicion_primo[num]:
        print(f"El producto de los dígitos de {num} es {producto}, no coincide con su posición en la lista de primos ({posicion_primo[num]})")
        return False
    else:
        print(f"El producto de los dígitos de {num} es {producto}, sí coincide con su posición en la lista de primos")



    num_espejo = espejo(num)
    if num_espejo not in primos:
        print(f"El número espejo de {num} es {num_espejo}, no es primo")
        return False
    else:
        print(f"El número espejo de {num} es {num_espejo}, sí es primo")

    posicion_espejo = espejo(posicion_primo[num])
    if posicion_espejo <= len(primos) and primos[posicion_espejo - 1] == num_espejo:
        print(f"El número {num} cumple con la conjetura de Sheldon")
        return True
    else:
        print(f"{num} no cumple con la conjetura de Sheldon como número espejo")
        return False

#Lista de numeros con sus posiciones
def generar_primos_y_posiciones(limite):
    primos = []
    posicion_primo = {}
    contador = 0

    for i in range(2, limite + 1):
        if es_num_primo(i):
            primos.append(i)
            contador = contador+1
            posicion_primo[i] = contador   

    return primos, posicion_primo


limite = 1_000_000
primos, posicion_primo = generar_primos_y_posiciones(limite)

# Comprobar si solo el 73 cumple la conjetura de Sheldon
for numero in range(1, limite + 1):
    if es_numero_sheldon(numero, primos, posicion_primo):
        print(f"\nEl número {numero} cumple con la Conjetura de Sheldon\n")
    else:
        print(f"El número {numero} no cumple con la Conjetura de Sheldon\n")
    if numero == 73:
        break  # Solo seguimos hasta verificar el 73 en este caso