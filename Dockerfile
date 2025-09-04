# Imagen base oficial de Python
FROM python:3.11-slim

# Configurar variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Realizar migraciones y recolectar archivos estáticos en tiempo de build
RUN python manage.py collectstatic --noinput

# Exponer el puerto que usará Gunicorn
EXPOSE 8000

# Comando de arranque para producción
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoP.wsgi:application"]


