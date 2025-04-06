# HPE CDS Tech Challenge 2024-25  Phase II
## Languages
- [ Español (ES)](#español-es)
- [ English (EN)](#english-en)

## Español (ES)
### Sobre el proyecto:
El proyecto consiste en la creación de una aplicación que ayude a fomentar el turismo ecológico.

### Cómo ejecutar el proyecto

#### Paso 0: Instalar docker y establecer variables de entorno

Docker (más información aquí: [https://www.docker.com](https://www.docker.com))\
Git (más información aquí: [https://git-scm.com](https://git-scm.com))

### Variables de Entorno

| Variable de entorno                          | Descripción                                                                                      | Valor por defecto                                                                                    | Obligatoria                      |
|----------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------|
| `SUSTAINABILITY_INDEX_ENERGY_IMPORTANCE`     | Importancia del uso de energía (0 a 1). La suma total no debe superar 1.                         | `0.4`                                                                                                 | ❌                                |
| `SUSTAINABILITY_INDEX_WASTE_IMPORTANCE`      | Importancia de la reducción de residuos (0 a 1). La suma total no debe superar 1.                | `0.2`                                                                                                 | ❌                                |
| `SUSTAINABILITY_INDEX_RECYCLING_IMPORTANCE`  | Importancia del reciclaje (0 a 1). La suma total no debe superar 1.                              | `0.3`                                                                                                 | ❌                                |
| `SUSTAINABILITY_INDEX_WATER_USAGE_IMPORTANCE`| Importancia del ahorro de agua (0 a 1). La suma total no debe superar 1.                         | `0.1`                                                                                                 | ❌                                |
| `JWT_SECRET_KEY`                             | Clave secreta para firmar tokens JWT                                                             | *(redactado)*                                                                                        | ❌                                |
| `JWT_ALGORITHM`                              | Algoritmo JWT permitido                                                                          | `[HS256, HS384, HS512, ES256, ES256K, ES384, ES512, RS256, RS384, RS512, PS256, PS384, PS512]`       | ❌                                |
| `JWT_EXPIRE_MINUTES`                         | Tiempo de expiración del JWT (en minutos)                                                        | `1440`                                                                                                | ❌                                |
| `SUPERADMIN_EMAIL`                           | Correo electrónico del superadministrador                                                        | `superadmin`                                                                                          | ❌                                |
| `SUPERADMIN_PASSWORD`                        | Contraseña del superadministrador                                                                | `0000`                                                                                                 | ❌                                |
| `EMBEDDINGS_GENERATION_BATCH_SIZE`           | Tamaño del lote para la generación de embeddings                                                 | `1000`                                                                                                | ❌                                |
| `VECTORDB_HOST`                              | Host de la base vectorial                                                                        | `localhost`                                                                                           | ❌                                |
| `VECTORDB_PORT`                              | Puerto de la base vectorial                                                                      | `6333`                                                                                                 | ❌                                |
| `OPENAI_API_KEY`                             | Clave de API de OpenAI                                                                           |                                                                                                      | ✅                                |
| `QDRANT_COLLECTION_NAME`                     | Nombre de la colección en la base vectorial                                                      | `Reviews`                                                                                             | ❌                                |
| `DB_HOST`                                    | Host de la base de datos relacional                                                              |                                                                                                      | ✅ *(No necesario con Docker)*   |
| `DB_USERNAME`                                | Usuario de la base de datos relacional                                                           |                                                                                                      | ✅ *(No necesario con Docker)*   |
| `DB_PASSWORD`                                | Contraseña de la base de datos relacional                                                        |                                                                                                      | ✅ *(No necesario con Docker)*   |
| `DB_PORT`                                    | Puerto de la base de datos relacional                                                            |                                                                                                      | ✅ *(No necesario con Docker)*   |



#### Paso 1
Clonar el proyecto
```shell
$ git clone https://github.com/EdgarAlcoba/CDSTC-2024-2025-FASE-2.git
```

```shell
MYSQL_DATABASE = Nombre de la base de datos
MYSQL_ROOT_PASSWORD = Contraseña del administrador de la base de datos
OPENAI_API_KEY = Api key de OpenAI
```
#### Paso 3:
=======
#### Paso 2:
>>>>>>> develop
Seleccionar el directorio en el que se haya clonado el repositorio y ejecutar el comando:  
```shell
$ docker-compose up --build
```

## English (EN)
### About the project:
The project consists of creating an application that helps promote eco-tourism.

### How to run the project

#### Step 0: Install Docker and set environment variables

Docker (more information here: [https://www.docker.com](https://www.docker.com))\
Git (more information here: [https://git-scm.com](https://git-scm.com))

## Environment Variables

| Environment Variable                        | Description                                                                                                                             | Default Value                                                                                              | Required                      |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------|
| SUSTAINABILITY_INDEX_ENERGY_IMPORTANCE      | Importance of energy usage in the sustainability index. Must be from 0 to 1. The sum of all importance values must not exceed 1         | 0.4                                                                                                        | ❌                             |
| SUSTAINABILITY_INDEX_WASTE_IMPORTANCE       | Importance of waste reduction in the sustainability index. Must be from 0 to 1. The sum of all importance values must not exceed 1      | 0.2                                                                                                        | ❌                             |
| SUSTAINABILITY_INDEX_RECYCLING_IMPORTANCE   | Importance of recycling in the sustainability index. Must be from 0 to 1. The sum of all importance values must not exceed 1            | 0.3                                                                                                        | ❌                             |
| SUSTAINABILITY_INDEX_WATER_USAGE_IMPORTANCE | Importance of reducing water usage in the sustainability index. Must be from 0 to 1. The sum of all importance values must not exceed 1 | 0.1                                                                                                        | ❌                             |
| JWT_SECRET_KEY                              | Secret key for Json Web Tokens                                                                                                          | (redacted)                                                                                                 | ❌                             |
| JWT_ALGORITHM                               | Algorithm used for Json Web Tokens                                                                                                      | Any of these: [HS256, HS384, HS512, ES256, ES256K, ES384, ES512, RS256, RS384, RS512, PS256, PS384, PS512] | ❌                             |
| JWT_EXPIRE_MINUTES                          | Token validity time in minutes                                                                                                          | 1440                                                                                                       | ❌                             |
| SUPERADMIN_EMAIL                            | Email of the admin user                                                                                                                 | superadmin                                                                                                 | ❌                             |
| SUPERADMIN_PASSWORD                         | Password of the admin user                                                                                                              | 0000                                                                                                       | ❌                             |
| EMBEDDINGS_GENERATION_BATCH_SIZE            | Batch size for vector database generation                                                                                               | 1000                                                                                                       | ❌                             |
| VECTORDB_HOST                               | Host of the vector database                                                                                                             | localhost                                                                                                  | ❌                             |
| VECTORDB_PORT                               | Port of the vector database                                                                                                             | 6333                                                                                                       | ❌                             |
| OPENAI_API_KEY                              | OpenAI API key                                                                                                                          |                                                                                                            | ✅                             |
| QDRANT_COLLECTION_NAME                      | Name of the vector database table                                                                                                       | Reviews                                                                                                    | ❌                             |
| DB_HOST                                     | Host of the relational database                                                                                                         |                                                                                                            | ✅  (Not required with Docker) |
| DB_USERNAME                                 | Username for the relational database                                                                                                    |                                                                                                            | ✅  (Not required with Docker) |
| DB_PASSWORD                                 | Password for the relational database                                                                                                    |                                                                                                            | ✅  (Not required with Docker) |
| DB_PORT                                     | Port of the relational database                                                                                                         |                                                                                                            | ✅  (Not required with Docker) |

#### Step 1:
Clone the project
```shell
$ git clone https://github.com/EdgarAlcoba/CDSTC-2024-2025-FASE-2.git
```

```shell
MYSQL_DATABASE = Name of MySQL database
MYSQL_ROOT_PASSWORD = Password for root user of MySQL database
OPENAI_API_KEY = Api key de OpenAI
```
#### Step 3:
Navigate to the directory where the repository was cloned and run the following command:
=======
#### Step 2:
Run the project
>>>>>>> develop
```shell
$ docker-compose up --build
```
