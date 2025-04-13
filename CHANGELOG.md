# CHANGELOG.md
## Dia 1 2025-04-09 - Configuracion inicial del entorno y estructura

- Se creo la carpeta del proyecto `PRUEBA_ENTRADA_CC3S2`
- Se instalo y configuro entorno virtual con FastAPI, Uvicorn, asyncpg, databases
- Se creo archivo `Dockerfile` para la app
- Se configuro `docker-compose.yml` con los servicios `app` y `db`
- Se incluyo el script `db/init.sql` con creacion de tabla `questions` y datos iniciales
- Se valido que el contenedor `db` se levanta correctamente y la tabla se crea con datos cargados
- Se creo la rama `feature/dia1` a partir de `develop`
- Se realizo merge a `develop` y se agrego tag `v1.0-day1`

**Tag asociado:** `v1.0-day1`


## Dia 2 - 2025-04-09 - Implementacion de modelo `Question`, conexion a base de datos y pruebas unitarias
- Se creo la clase `Question` en el archivo `question.py` con los atributos `description`, `options`, `correct_index` y `difficulty`, y el metodo `is_correct()`
- Se implemento la funcion `get_questions_from_db()` en `database.py` para recuperar preguntas desde PostgreSQL usando `psycopg2`
- Se agrego manejo de errores en `is_correct()` para lanzar excepcion `TypeError` si el indice de respuesta no es un entero
- Se organizaron los archivos de la aplicacion en modulos separados: `question.py`, `database.py`, y `main.py`
- Se escribieron pruebas unitarias para la clase `Question` en `tests/test_question.py` utilizando `pytest`
- Se agrego un test de integracion para validar que `get_questions_from_db()` retorna una lista de preguntas validas desde la base de datos
- Se incluyo `pytest` en `requirements.txt`
- Se configuro un nuevo servicio `test` en `docker-compose.yml` para ejecutar pruebas automaticamente dentro del entorno Docker
- Se actualizo el `Dockerfile` para soportar pruebas y estructuras modulares
- Se verifico que los tests se ejecuten correctamente con el comando `docker-compose run --rm test`
- Se creo la rama `feature/dia2` desde `develop`, se integraron los cambios y se realizo merge a `develop`
- Se agrego tag `v2.0-day2`

**Tag asociado:** `v1.0-day2`


## Dia 3 - 2025-04-10 - Implementacion de la clase `Quiz` y flujo basico del juego
- Implementacion de la clase `Quiz`
- en la funcion `main()` se simula el flujo basico del juego mostrando preguntas en consola
- Conexion con la logica de `Question` y obtencion de preguntas desde la base de datos
- Se creo la rama `feature/dia3-estructura-basic` desde `develop`, se integraron los cambios y se realizo merge a `develop`

**Tag asociado:** `v1.0-day3`


## Dia 5- 2025-04-10 - 