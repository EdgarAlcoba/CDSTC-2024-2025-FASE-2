@echo off
echo Iniciando docker-compose...

:: Verifica si Docker está corriendo
docker info >nul 2>&1
IF ERRORLEVEL 1 (
    echo Docker no está corriendo o no está instalado.
    pause
    exit /b 1
)

:: Ejecutar docker-compose up
docker-compose up -d

:: Mostrar estado de los contenedores
docker-compose ps

echo Contenedores iniciados correctamente.
pause
