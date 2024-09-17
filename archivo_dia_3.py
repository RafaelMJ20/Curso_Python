# Constantes en Python
# Rafael Miranda Jimenez
import math


print('*** Constantes en Python ***')

PI = 3.14159
print('El valor de PI es: ', PI)

NOMBRE_BASE_DATOS = 'clientes_db'
print('Nombre de la base de datos: ', NOMBRE_BASE_DATOS)

# Esto NO se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = 'cliente_db'
print('No cambiar el valor de una constante: ', NOMBRE_BASE_DATOS)

# Usar una constante del lenguaje Python
print('Valor de math.pi: ', math.pi)