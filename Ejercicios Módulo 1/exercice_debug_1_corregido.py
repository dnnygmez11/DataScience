
#EJERCICIO 5 CORREGIDO

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
