# APP name
## Languages
- [ 🇪🇸 Spanish (ESP)](#spanish-esp)
- [ 🇬🇧 English (EN)](#english-en)

## Spanish (ESP)
### Sobre el proyecto:
El proyecto consiste en la creación de una aplicación que ayude a fomentar el turismo ecológico.

### Cómo ejecutar el proyecto
#### Software necesario:
Docker (más información aquí: [https://www.docker.com](https://www.docker.com))
#### Paso 1:
Clonar el proyecto
```shell
$ git clone https://github.com/EdgarAlcoba/CDSTC_2024-2025-FASE-2.git
```
#### Paso 2:
Es necesario modificar las siguientes variables de entorno en el archivo docker-compose o incluirlas en tu sistema operativo  

```shell
MYSQL_DATABASE = Nombre de la base de datos
MYSQL_ROOT_PASSWORD = Contraseña de la base de datos
NODE_ENV = DEV ó PROD
OPENAI_API_KEY = Api key de OpenAI
```
#### Paso 3:
Seleccionar el directorio en el que se haya clonado el repositorio y ejecutar el comando:  
```shell
$ docker-compose up --build
```

## English (EN)
### About the project
The project consists of creating an application that helps promote ecological tourism.

### How to run the project
#### Software necesario:
Docker (more information here: [https://www.docker.com](https://www.docker.com))

#### Step 1:
Clonar el proyecto
```shell
$ git clone https://github.com/EdgarAlcoba/CDSTC_2024-2025-FASE-2.git
```
#### Step 2:
Modify the following environment variables in the docker-compose file or add them to your operating system:

```shell
MYSQL_DATABASE = Name of MySQL database
MYSQL_ROOT_PASSWORD = Password for root user of MySQL database
NODE_ENV = DEV ó PROD
OPENAI_API_KEY = Api key de OpenAI
```
#### Step 3:
Navigate to the directory where the repository was cloned and run the following command:
```shell
$ docker-compose up --build
```