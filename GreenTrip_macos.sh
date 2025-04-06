#!/bin/zsh

# Nombre del archivo: levantar_contenedores.sh

# Salir si ocurre un error
set -e

# Verificar si docker-compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "Error: docker-compose no está instalado."
    exit 1
fi

# Ejecutar docker-compose up
echo "Levantando los contenedores con docker-compose..."
docker-compose up -d

# Mostrar el estado de los contenedores
echo "Estado de los contenedores:"
docker-compose ps
