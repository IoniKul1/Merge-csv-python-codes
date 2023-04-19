import pandas as pd

# Leer archivo CSV
df = pd.read_csv('resultado_filtrado_4.csv')

# Convertir la columna 'fecha_ingreso' y 'fecha_cierre_contacto' a tipo de dato fecha
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df['fecha_cierre_contacto'] = pd.to_datetime(df['fecha_cierre_contacto'])

# Calcular la duración total en días
df['duracion_total'] = (df['fecha_cierre_contacto'] - df['fecha_ingreso']).dt.days

# Agrupar por 'domicilio_barrio' y calcular la suma de 'dias_diferencia' y dividir por 'cantidad_denuncias'
df['duracion_total'] = df.groupby('domicilio_barrio')['dias_diferencia'].transform('sum') / df['cantidad_denuncias']

df.to_csv('resultado_filtrado_5.csv', index=False)

