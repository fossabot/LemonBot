[![Code Health](https://landscape.io/github/LemonDevelopment/LemonBot/master/landscape.svg?style=flat-square)](https://landscape.io/github/LemonDevelopment/LemonBot/master)
# LemonBot: Un humilde Bot de Discord.
LemonBot es un Bot de Discord creado para mejorar o ampliar funciones que no existen en bots actuales.

# Ejecucion
Personalmente no me gustaria que ejecutes el Bot por tu cuenta, en cambio pueds [invitarlo](https://discordapp.com/oauth2/authorize?client_id=358031514749108228&scope=bot&permissions=37112833) a tu servidor.

Igual si aun deseas probarlo localmente crea un archivo llamado **config.py** con la configuracion ajustada a tus necesidades.

# Ejemplo de Configuracion
Aqui puedes ver un ejemplo del archivo de configuracion, personaliza estos valores si es que quieres hostear el Bot personalmente.

```py
token = "XXXXXXXXXXXX" # Token de Discord
genius = "XXXXXXXXXXXX" # Access de Genius
prefix = "." # Prefijo
lang = "es-CL" # Idioma del Bot
dev = False # Modo desarrollo activado o desactivado
use_mysql = True # Si deseas usar una Base de Datos MySQL
mysql_ip = "127.0.0.1" # Direccion de MySQL
mysql_port = "3306" # Puerto de MySQL
mysql_user = "lemonbot" # Usuario en MySQL
mysql_pass = "XXXXXXXXXXXX" # Usuario en MySQL
mysql_db = "lemonbot" # Base de Datos en el Servidor
```

# Creando la base de datos y el usuario
Si sabes como crear una base de datos y establecer permisos salta esta opcion. Puedes ejecutar estos comandos para crear un usuario con su base de datos.

Recuerda reemplazar **password** con la contraseña que desees usar.

```sql
CREATE USER 'lemonbot'@'localhost' IDENTIFIED BY 'password'; 
CREATE USER 'lemonbot'@'%' IDENTIFIED BY 'password';
CREATE DATABASE 'lemonbot';
GRANT ALL PRIVILEGES ON 'lemonbot'.* TO 'lemonbot'@'localhost';
GRANT ALL PRIVILEGES ON 'lemonbot'.* TO 'lemonbot'@'%';
```
