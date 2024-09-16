import websocket
import json
from kafka import KafkaProducer

# Configuration du producteur Kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def on_message(ws, message):
    data = json.loads(message)
    
    # Extraire les informations importantes : prix d'achat, prix de vente, volume
    buy_price = float(data['b'])
    sell_price = float(data['a'])
    volume = float(data['A'])
    timestamp = data['E']
    
    # Créer un message Kafka
    bitcoin_data = {
        "timestamp": timestamp,
        "buy_price": buy_price,
        "sell_price": sell_price,
        "volume": volume
    }

    # Envoyer les données au topic Kafka
    producer.send('bitcoin_prices', value=bitcoin_data)
    print(f"Envoyé : {bitcoin_data}")

def on_error(ws, error):
    print(f"Erreur : {error}")

def on_close(ws):
    print("### WebSocket fermé ###")

def on_open(ws):
    # S'abonner au WebSocket pour recevoir les données sur le Bitcoin (symbol BTCUSDT)
    ws.send(json.dumps({"method": "SUBSCRIBE", "params": ["btcusdt@bookTicker"], "id": 1}))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@bookTicker",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
