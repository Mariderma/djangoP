# Usa una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto en el que corre Django
EXPOSE 8000

# Comando para correr el servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoP.wsgi:application"]

