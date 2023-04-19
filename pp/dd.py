import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('resultado.csv')

# Calcular la cantidad de apariciones de cada elemento en la columna 'domicilio_barrio'
apariciones = df['domicilio_barrio'].value_counts()

# Mostrar los resultados
print(apariciones)