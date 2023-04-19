import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('Barrios.csv')

# Eliminar los espacios en los nombres de las columnas
df.columns = df.columns.str.strip()

# Crear la nueva columna "ratio" calculando la división de "cantidad_denuncias" entre "densidad_habitantes"
df['ratio'] = df['cantidad_denuncias'] / df['densidad_habitantes']

df.to_csv('Barrios_2.csv', index=False)

# Mostrar el DataFrame con la nueva columna "ratio"