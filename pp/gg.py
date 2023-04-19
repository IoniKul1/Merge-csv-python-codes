import pandas as pd
from datetime import datetime

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('resultado_filtrado_3.csv')

# Convertir las columnas de fecha a objetos de tipo datetime
df['fecha_cierre_contacto'] = pd.to_datetime(df['fecha_cierre_contacto'], format='%d/%m/%Y')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'], format='%d/%m/%Y')

# Restar las fechas para obtener la diferencia en días
df['dias_diferencia'] = (df['fecha_cierre_contacto'] - df['fecha_ingreso']).dt.days

df.to_csv('resultado_filtrado_4.csv', index=False)
