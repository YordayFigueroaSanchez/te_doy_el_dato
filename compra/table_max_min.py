# Primero, importamos las librerías necesarias
import os
import pandas as pd
import matplotlib.pyplot as plt

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()

# Crear la carpeta 'datos_binance' en el directorio de trabajo, si no existe
carpeta_destino = os.path.join(directorio_actual, 'compra', 'datos_binance')

# Cargamos el archivo CSV (asumiendo que el archivo ya fue cargado en el entorno)
df = pd.read_csv(f"{carpeta_destino}/maximos_minimos_2024.csv")

# Convertimos la columna 'hour' a tipo datetime para trabajar con las fechas y horas
df['hour'] = pd.to_datetime(df['hour'])

# Extraemos la fecha, la hora y el día de la semana (0=lunes, 6=domingo)
df['date'] = df['hour'].dt.date
df['hour_of_day'] = df['hour'].dt.hour
df['day_of_week'] = df['hour'].dt.weekday  # Lunes=0, Domingo=6

# Calculamos el promedio de los valores 'high' y 'low' por hora
df['avg_price'] = (df['high'] + df['low']) / 2

# Agregar una nueva columna que muestra el lugar del 'avg_price' de esa hora comparado con los demás del mismo día
df['rank_of_day'] = df.groupby('date')['avg_price'].rank(method='min', ascending=False)

# imprimir
print(df)

# Creamos la tabla pivotada con las horas como filas, los días de la semana como columnas, y la suma de 'rank_of_day' como valores
pivot_table = df.pivot_table(
    values='rank_of_day', 
    index='hour_of_day', 
    columns='day_of_week', 
    aggfunc='sum', 
    fill_value=0
)

# Renombramos los días de la semana para que sea más legible
pivot_table.columns = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Encontramos la hora y el día con el valor máximo
max_value = pivot_table.max().max()  # Máximo valor en toda la tabla
max_position = pivot_table.stack().idxmax()  # Hora y día con el valor máximo

# Encontramos la hora y el día con el valor mínimo
min_value = pivot_table.min().min()  # Mínimo valor en toda la tabla
min_position = pivot_table.stack().idxmin()  # Hora y día con el valor mínimo

# Mostramos los resultados
print(pivot_table)

# Mostramos los resultados
print(f"El valor máximo es {max_value}, que corresponde a la hora {max_position[0]} en el día {max_position[1]}. Corresponde a mejor compra--OK")
print(f"El valor mínimo es {min_value}, que corresponde a la hora {min_position[0]} en el día {min_position[1]}. Corresponde a peor compra.")