#PARA EJERCICIO 3
import pandas as pd
import numpy as np

#EJERCICIO 1

def imprime_73(x):
  for i in range(x):
      print("Hello world")

imprime_73(73)

#EJERCICIO 2
def fibbo(x):
  a, b = 0, 1
  #uso x - 1 porque empieza desde 0 
  for i in range(x-1): 
      a, b = b, a + b
  print("El ",str(x)," número Fibbonacci es:", a)

fibbo(73)

#EJERCICIO 3

#SE IMPORTARON LAS LIBRERIAS DESDE EL INICIO

t_valores = np.arange(0, 4.02, 0.02)

df = pd.DataFrame({
    't': t_valores,  
    's': np.sin(t_valores)
})

df['s10'] = df['s'].shift(-10)

df['d'] = df['s'] - df['s10']

# 1 si d es positivo / 0 si es negativo
df['p'] = np.where(df['d'] > 0, 1, 0)

print(df)

df.to_csv("res_ejercicio3.csv", sep=';', index=False) 


#EJERCICIO 4

df = pd.read_csv("res_ejercicio3.csv", sep=';')

media_pos = df[df['p'] == 1]['d'].mean()
media_neg = df[df['p'] == 0]['d'].mean()

# Crear la columna 'm' con la media de acuerdo al valor de 'p'
df['m'] = df['p'].apply(lambda x: media_pos if x == 1 else media_neg)

suma_pos = df[df['d'] > 0]['d'].sum()
suma_neg = df[df['d'] < 0]['d'].sum()

resultado_df = pd.DataFrame({
    'tipo': ['negativos', 'positivos'],
    'suma_d': [suma_neg, suma_pos]
})

print(resultado_df)


#EJERCICIO 5
# STEP 1
print('STEP 1')

for i in range(0, 11):
    x = i

print(f'x should be 10: {x}')
if x == 10:
    print('SUCCESS! IN STEP 1')

# STEP 2
print('STEP 2')
x = True  #INICIALIZAMOS X COMO TRUE

for i in range(0, 11):
    if i == 5:
        x = x and True  #PARA CUMPLIR LA CONDICION X TIENE QUE SER TRUE
        break

print(f'x should be True: {x}')
print(f'i should be 5: {i}')
if i == 5 and x:
    print('SUCCESS! IN STEP 2')

#EJERCICO 6

def es_num_primo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

 
def num_primo(es_num_primo):
    contador_primos = 0   
    num = 1    

    while contador_primos < 73:
        num += 1
        if es_num_primo(num):
            contador_primos += 1 

    print("El número primo 73 es:", num)

num_primo(es_num_primo)


#EJERCICIO 7

def encontrar_intervalo_no_primos():
    num = 2  #primer num primo
    consecutivos_no_primos = 0  # Contador de números no primos consecutivos
    
    while True:
        # Verificar si el número no es primo
        if not es_num_primo(num):
            consecutivos_no_primos += 1  # Incrementamos el contador si no es primo
        else:
            consecutivos_no_primos = 0  # Reiniciamos si encontramos un primo
        
        # Verificamos si alcanzamos 73 números no primos consecutivos
        if consecutivos_no_primos == 73:
            
            inicio_intervalo = num - 72
            intervalo = list(range(inicio_intervalo, num + 1))  
            print("Intervalo de 73 números no primos consecutivos:")
            for valor in intervalo:
                print(valor)
            
            break  
        num += 1  

# Llamar a la función
encontrar_intervalo_no_primos()