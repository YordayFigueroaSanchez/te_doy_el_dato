import os
import requests
import pandas as pd
from datetime import datetime, timedelta

# Función para obtener los datos de candlesticks de Binance
def obtener_datos_binance(symbol, intervalo, limit=1000, inicio_timestamp=None):
    url = f'https://api.binance.com/api/v1/klines'
    params = {
        'symbol': symbol,
        'interval': intervalo,
        'limit': limit,
    }
    if inicio_timestamp:
        params['startTime'] = inicio_timestamp
    respuesta = requests.get(url, params=params)
    return respuesta.json()

# Función para obtener máximos y mínimos por hora para el mes de enero
def obtener_maximos_minimos(symbol, intervalo, mes=1, ano=2024):
    # Definir el rango de fechas (enero de 2024)
    inicio_enero = datetime(ano, mes, 1)  # 1 de enero de 2024
    fin_enero = datetime(ano, mes + 1, 1) - timedelta(seconds=1)
    # fin_enero = datetime(2025, 1, 1) - timedelta(seconds=1)
    
    # Convertir a timestamps en milisegundos
    timestamp_inicio = int(inicio_enero.timestamp() * 1000)
    timestamp_fin = int(fin_enero.timestamp() * 1000)

    # Obtener los datos de Binance con múltiples solicitudes si es necesario
    datos = []
    next_start_time = timestamp_inicio
    while next_start_time < timestamp_fin:
        datos_parciales = obtener_datos_binance(symbol, intervalo, limit=1000, inicio_timestamp=next_start_time)
        if not datos_parciales:
            break
        datos.extend(datos_parciales)
        next_start_time = datos_parciales[-1][0] + 1  # El siguiente timestamp de inicio
    
    # Filtrar los datos en el rango de fechas deseado
    datos_filtrados = [kline for kline in datos if timestamp_inicio <= kline[0] <= timestamp_fin]
    
    # Convertir a un DataFrame para facilidad de manejo
    df = pd.DataFrame(datos_filtrados, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    
    # Convertir las columnas relevantes a números
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    
    # Convertir el timestamp a formato legible
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Agrupar por hora y obtener los máximos y mínimos por cada hora
    df['hour'] = df['timestamp'].dt.floor('h')
    max_min_por_hora = df.groupby('hour').agg({'high': 'max', 'low': 'min'}).reset_index()

    # Obtener el directorio de trabajo actual
    directorio_actual = os.getcwd()

    # Crear la carpeta 'datos_binance' en el directorio de trabajo, si no existe
    carpeta_destino = os.path.join(directorio_actual, 'compra', 'datos_binance')
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Guardar los resultados en un archivo CSV dentro de la carpeta
    archivo_csv = os.path.join(carpeta_destino, 'maximos_minimos_'+ str(mes) +'_2024.csv')
    max_min_por_hora.to_csv(archivo_csv, index=False)
    
    print(f"Datos guardados en '{archivo_csv}'")
    return max_min_por_hora

# Ejemplo de uso
symbol = 'BTCUSDT'
intervalo = '1h'  # Intervalo de una hora

max_min = obtener_maximos_minimos(symbol, intervalo, mes=12, ano=2024)

# Mostrar los resultados
print(max_min)
