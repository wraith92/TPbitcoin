# Utiliser une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier les fichiers locaux dans le conteneur
COPY . .

# Installer les dépendances Python à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter le script websocket_bitcoin.py
CMD ["python", "websocket_bitcoin.py"]
