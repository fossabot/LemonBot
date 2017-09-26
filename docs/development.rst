.. _development:

Desarrollo
===========

Para probar el Bot de manera local mientras preparas tus aportes, debes establecer un par de cosas:

Requisitos
-----------

- Python 3.5 o superior
    - Discord.py 1.0 o superior (aka *rewrite*)
    - YouTube-dl (para audio)
    - Requests
    - BeautifulSoup 4
- FFMpeg 3 o superior en PATH (para audio)

Configuracion
--------------

Crea un archivo llamado **config.py** en la Raiz del repositorio con el siguiente formato e informacion:

.. code-block:: Python

    token = "XXXXXXXXXXXX" # Token de acceso a Discord
    genius = "XXXXXXXXXXXX" # Token de acceso a Genius
    prefix = "." # Prefijo de los comandos del Bot
    lang = "es-CL" # Idioma de la carpeta "strings"
    dev = False # Activa el modo desarrollo: muestra los errores tal cual
    use_mysql = True # Activa el uso de una Base de Datos MySQL (opcional)

    mysql_loc = "127.0.0.1:3306" # Direccion de la Base de Datos MySQL
    mysql_user = "lemonbot" # Usuario con acceso a MySQL
    mysql_pass = "XXXXXXXXXXXX" # Contraseña del usuario
    mysql_db = "lemonbot" # Base de Datos a usar

.. note::

    Este archivo no sera subido al crear Commits o Pull Requests

Base de Datos
--------------

Puedes ejecutar estos comandos en MySQL para crear un usuario con su base de datos. Recuerda reemplazar **password** con la contraseña que desees usar.

.. code-block:: mysql

    CREATE DATABASE 'lemonbot';
    CREATE USER 'lemonbot'@'localhost' IDENTIFIED BY 'password'; 
    CREATE USER 'lemonbot'@'%' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON 'lemonbot'.* TO 'lemonbot'@'localhost';
    GRANT ALL PRIVILEGES ON 'lemonbot'.* TO 'lemonbot'@'%';
    FLUSH PRIVILEGES;
