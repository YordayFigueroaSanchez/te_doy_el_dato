import requests
import pandas as pd
from datetime import datetime, timedelta

# Funcin para obtener los datos de candlesticks de Binance
def obtener_datos_binance(symbol, intervalo, limit=1000):
    url = f'https://api.binance.com/api/v1/klines'
    params = {
        'symbol': symbol,
        'interval': intervalo,
        'limit': limit,
    }
    respuesta = requests.get(url, params=params)
    return respuesta.json()

# Funcin para obtener mximos y mnimos por hora para las ltimas 24 horas
def obtener_maximos_minimos(symbol, intervalo, periodo_dias=1):
    # Definir el rango de fechas (ltimas 24 horas)
    ahora = datetime.utcnow()
    hace_24_horas = ahora - timedelta(hours=periodo_dias * 24)

    # Convertir a timestamps en milisegundos
    timestamp_ahora = int(ahora.timestamp() * 1000)
    timestamp_hace_24_horas = int(hace_24_horas.timestamp() * 1000)

    # Obtener los datos de Binance
    datos = obtener_datos_binance(symbol, intervalo)

    # Filtrar los datos en el rango de fechas deseado
    datos_filtrados = []
    for kline in datos:
        timestamp_kline = kline[0]
        if timestamp_kline >= timestamp_hace_24_horas and timestamp_kline <= timestamp_ahora:
            datos_filtrados.append(kline)
    
    # Convertir a un DataFrame para facilidad de manejo
    df = pd.DataFrame(datos_filtrados, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    
    # Convertir las columnas relevantes a nmeros
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    
    # Convertir el timestamp a formato legible
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Agrupar por hora y obtener los mximos y mnimos por cada hora
    df['hour'] = df['timestamp'].dt.floor('H')
    max_min_por_hora = df.groupby('hour').agg({'high': 'max', 'low': 'min'}).reset_index()

    # Guardar los resultados en un archivo CSV
    max_min_por_hora.to_csv('maximos_minimos_ultima_24h.csv', index=False)
    
    print("Datos guardados en 'maximos_minimos_ultima_24h.csv'")
    return max_min_por_hora

# Ejemplo de uso
symbol = 'BTCUSDT'
intervalo = '1h'  # Intervalo de una hora

max_min = obtener_maximos_minimos(symbol, intervalo)

# Mostrar los resultados
print(max_min)