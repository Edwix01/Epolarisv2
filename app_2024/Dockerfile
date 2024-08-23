# Usa una imagen base de Node.js
FROM node:20.12.2

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app_2024

# Copia el archivo package.json y package-lock.json al directorio de trabajo
COPY . .  

# Instala las dependencias
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# Crea un entorno virtual de Python
RUN python3 -m venv /app/venv

# Activa el entorno virtual y actualiza pip
RUN /app/venv/bin/pip install --upgrade pip

# Copia el archivo requirements.txt y utiliza el entorno virtual para instalar dependencias
RUN /app/venv/bin/pip install -r requirements.txt


RUN npm install

# Expone el puerto en el que se ejecuta la aplicación (por defecto 3000)
EXPOSE 443

# Comando para ejecutar la aplicación
CMD ["node", "./src/app.js"]

