# Image de base Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY simple_math.py .
COPY test_simple_math.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut : exécuter les tests unitaires
CMD ["python", "-m", "unittest", "test_simple_math", "-v"]
