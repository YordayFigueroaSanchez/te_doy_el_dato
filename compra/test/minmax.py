import requests
import pandas as pd
from datetime import datetime, timedelta

# Funcion para obtener los datos de candlesticks de Binance
def obtener_datos_binance(symbol, intervalo, limit=1000):
    url = f'https://api.binance.com/api/v1/klines'
    params = {
        'symbol': symbol,
        'interval': intervalo,
        'limit': limit,
    }
    respuesta = requests.get(url, params=params)
    return respuesta.json()

# Funcion para procesar los datos y obtener maximos y minimos
def obtener_maximos_minimos(symbol, intervalo, periodo_dias=30):
    # Definir el rango de fechas
    ahora = datetime.utcnow()
    hace_30_dias = ahora - timedelta(days=periodo_dias)

    # Convertir a timestamps en milisegundos
    timestamp_ahora = int(ahora.timestamp() * 1000)
    timestamp_hace_30_dias = int(hace_30_dias.timestamp() * 1000)

    # Obtener los datos de Binance
    datos = obtener_datos_binance(symbol, intervalo)

    # Filtrar los datos en el rango de fechas deseado
    datos_filtrados = []
    for kline in datos:
        timestamp_kline = kline[0]
        if timestamp_kline >= timestamp_hace_30_dias and timestamp_kline <= timestamp_ahora:
            datos_filtrados.append(kline)
    
    # Convertir a un DataFrame para facilidad de manejo
    df = pd.DataFrame(datos_filtrados, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    
    # Convertir las columnas relevantes a numeros
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])

    # Obtener los maximos y minimos del ultimo mes
    maximo = df['high'].max()
    minimo = df['low'].min()
    
    return maximo, minimo

# Ejemplo de uso
symbol = 'BTCUSDT'
intervalo = '1d'  # Intervalo de un dia

maximo, minimo = obtener_maximos_minimos(symbol, intervalo)

print(f"Maximo de BTC/USDT en el ultimo mes: {maximo}")
print(f"Minimo de BTC/USDT en el ultimo mes: {minimo}")
