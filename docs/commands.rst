.. _commands:

Comandos
=========
Esta es la lista de comandos disponibles, los parametros pueden ser <obligatorios> u [opcionales].

.. contents::
    :local:

General
--------
.. code::

    .info

Muestra informacion general sobre el Bot tales como la version, soporte y repositorio.

.. code::

    .help

Devuelve un enlace a esta pagina para ver los comandos del Bot.

Musica
-------
.. code::

    .lyrics <cancion>

Busca y obtiene las letras de una cancion desde Genius_.

Si esta tiene mas de 2048 caracteres, se mostrara el enlace a la pagina (es una limitacion de la API de Discord, no se puede hacer nada).

Herramientas del Dueño
-----------------------
.. note::

    Estos comandos estan diseñados para ser usados por el usuario que registro el token del Bot.

    Si crees que necesitas usar uno de estos contacta al desarrollador. 

.. code::

    .shutdown

Cierra la sesion del Bot y se desconecta satisfactoriamente.

.. code::

    .guilds

Muestra una lista Guilds / Servidores a las que el Bot tiene acceso junto al numero de estas.

.. code::

    .load <addon>

.. code::

    .unload <addon>

Carga o Descarga un Addon o Cog desde su respectiva carpeta.

Reproductor de Musica
----------------------
.. warning::

    Los comandos relacionados a Audio estan en fase Beta. USALOS BAJO TU PROPIO RIESGO!

.. code::

    .join

Si el autor del comando esta en un canal de voz, el Bot se unira a este.

.. code::

    .play <search|url>

Busca un video en YouTube o especifica una URL para reproducir. Puedes encontrar una lista de servicios disponibles en la pagina web de YouTubeDl_.

.. code::

    .volume <percentage>

Establece el volumen del reproductor. El parametro esta basado en porcentaje, en donde 1 es 1% y 75 es 75%.

.. code::

    .stop

Detiene la reproduccion y deja el canal de voz.

.. _YouTubeDl: https://rg3.github.io/youtube-dl/supportedsites.html
.. _Genius: https://genius.com
