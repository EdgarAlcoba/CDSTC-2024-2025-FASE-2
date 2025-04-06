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

## Variables de entorno

| Variable de entorno                         | Descripción                                                                                                                                              | Valor por defecto                                                                                    | Obligatoria                  |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------|
| SUSTAINABILITY_INDEX_ENERGY_IMPORTANCE      | Importancia del uso de energía en el índice de sostenibilidad. Debe ser de 0 a 1. La suma de todas las importancias no pueden superar 1                  | 0.4                                                                                                  | ❌                            |
| SUSTAINABILITY_INDEX_WASTE_IMPORTANCE       | Importancia de la reducción de residuos en el índice de sostenibilidad. Debe ser de 0 a 1. La suma de todas las importancias no pueden superar 1         | 0.2                                                                                                  | ❌                            |
| SUSTAINABILITY_INDEX_RECYCLING_IMPORTANCE   | Importancia del reciclaje en el índice de sostenibilidad. Debe ser de 0 a 1. La suma de todas las importancias no pueden superar 1                       | 0.3                                                                                                  | ❌                            |
| SUSTAINABILITY_INDEX_WATER_USAGE_IMPORTANCE | Importancia de la reducción del consumo de agua en el índice de sostenibilidad. Debe ser de 0 a 1. La suma de todas las importancias no pueden superar 1 | 0.1                                                                                                  | ❌                            |
| JWT_SECRET_KEY                              | Clave secreta del Json Web Tokens                                                                                                                        | (redacted)                                                                                           | ❌                            |
| JWT_ALGORITHM                               | Algoritmo usado para el Json Web Tokens                                                                                                                  | Any of these: [HS256, HS384, HS512, ES256, ES256K, ES384, ES512,RS256,RS384,RS512,PS256,PS384,PS512] | ❌                            |
| JWT_EXPIRE_MINUTES                          | Tiempo de validez del token en minutos                                                                                                                   | 1440                                                                                                 | ❌                            |
| SUPERADMIN_EMAIL                            | Correo de usuario del usuario de administrador                                                                                                           | superadmin                                                                                           | ❌                            |
| SUPERADMIN_PASSWORD                         | Contraseña del usuario administrador                                                                                                                     | 0000                                                                                                 | ❌                            |
| EMBEDDINGS_GENERATION_BATCH_SIZE            | Tamaño del batch de la generación de la base de datos vectorial                                                                                          | 1000                                                                                                 | ❌                            |
| VECTORDB_HOST                               | Host de la base de datos vectorial                                                                                                                       | localhost                                                                                            | ❌                            |
| VECTORDB_PORT                               | Puerto de la base de datos vectorial                                                                                                                     | 6333                                                                                                 | ❌                            |                                                                                      
| OPENAI_API_KEY                              | Clave de API de OpenAI                                                                                                                                   |                                                                                                      | ✅                            |
| QDRANT_COLLECTION_NAME                      | Nombre de la tabla de la base de datos vectorial                                                                                                         | Reviews                                                                                              | ❌                            |
| DB_HOST                                     | Host de la base de datos relacional                                                                                                                      |                                                                                                      | ✅  (No necesario con Docker) |
| DB_USERNAME                                 | Nombre de usuario de la base de datos relacional                                                                                                         |                                                                                                      | ✅  (No necesario con Docker) |
| DB_PASSWORD                                 | Contraseña de la base de datos relacional                                                                                                                |                                                                                                      | ✅  (No necesario con Docker) |
| DB_PORT                                     | Puerto de la base de datos relacional                                                                                                                    |                                                                                                      | ✅  (No necesario con Docker) |


#### Paso 1:
Clonar el proyecto
```shell
$ git clone https://github.com/EdgarAlcoba/CDSTC_2024-2025-FASE-2.git
```

#### Paso 2:
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
$ git clone https://github.com/EdgarAlcoba/CDSTC_2024-2025-FASE-2.git
```

#### Step 2:
Run the project
```shell
$ docker-compose up --build
```
