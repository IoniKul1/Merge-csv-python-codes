import pandas as pd

# Cargar los dos conjuntos de datos en DataFrames
df1 = pd.read_csv('Barrios_2.csv', sep=',')
df2 = pd.read_csv('vme.csv', sep=';')

# Unir los DataFrames por la columna "domicilio_barrio"
df_result = pd.merge(df2, df1, on='domicilio_barrio', how='left')
print(df_result.head)
df_result.to_csv('resultado_filtrado_3.csv', index=False)

# Filtrar las columnas "domicilio_barrio" y "densidad_habitantes"
#df_result_filtered = df_result[['domicilio_barrio', 'densidad_habitantes', 'cantidad_denuncias']]

# Eliminar duplicados en la columna "domicilio_barrio"
#df_result_filtered = df_result_filtered.drop_duplicates(subset='domicilio_barrio')

# Guardar el resultado filtrado en un nuevo archivo CSV
#df_result_filtered.to_csv('resultado_filtrado.csv', index=False)
