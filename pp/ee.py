import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('resultado.csv')

apariciones = (df['fecha_cierre_contacto'] - df['fecha_ingreso'])% df['cantidad_denuncias']

# Mostrar los resultados
print(apariciones)