---
#post: "&nbsp;👋"
title: Tutorial de Django
description: Tutorial de Django
weight: 30
alwaysopen: false
---

Django (gdh/ˈdʒæŋɡoʊ/jang-goh) es un framework para aplicaciones web gratuito y open source, escrito en Python. Es un WEB framework - un conjunto de componentes que te ayudan a desarrollar sitios web más fácil y rápido.

Cuando estás construyendo un sitio web, frecuentemente se necesitan un conjunto de componentes similares: una manera de manejar la autenticación de usuarios (registrarse, iniciar sesión, cerrar sesión), un panel de administración para tu sitio web, formularios, una forma de subir archivos, entre otras cosas.

Los frameworks existen para ahorrarte tener que reinventar la rueda y ayudar a aliviar la carga cuando se construye un sitio.

## Para que ocupamos un framework

Para entender para qué es Django, necesitamos mirar más de cerca a los servidores. Lo primero es que el servidor sepa que quieres que te sirva una página web.

Imagina un buzón (puerto) el cual es monitoreado para cartas entrantes (peticiones). Esto es realizado por un servidor web. El servidor web lee la carta, y envía una respuesta con una página web. Pero cuando quieres enviar algo, tienes que tener algún contenido. Y Django es algo que te ayuda a crear el contenido.

### Flujo de una petición

Cuando llega una petición a un servidor web, ésta es pasada a Django, el cual intenta averiguar lo que realmente es solicitado. Toma primero una dirección de página web y trata de averiguar qué hacer. Esta parte es realizada por el `urlresolver` de Django (ten en cuenta que la dirección de un sitio web es llamada URL (_Uniform Resource Locator_) - así que el nombre `urlresolver` tiene sentido). Este no es muy inteligente - toma una lista de patrones y trata de encontrar la URL. Django comprueba los patrones de arriba hacia abajo y si algo coincide entonces Django le pasa la solicitud a la función asociada (que se llama **vista**).

Imagina a un cartero llevando una carta. Él está caminando por la calle y comprueba cada número de casa con el que está en la carta. Si coincide, él deja la carta allí. Esto es similar al funcionamiento del `urlresolver`.

En la función de **vista** se hacen todas las cosas interesantes: podemos mirar a una base de datos para buscar alguna información. ¿Tal vez el usuario pidió cambiar algo en los datos? Como una carta diciendo "Por favor cambia la descripción de mi trabajo." La vista puede comprobar si tienes permitido hacer eso, entonces actualizar la descripción del trabajo para ti y devolverte un mensaje: "¡hecho!". Entonces la **vista** genera una respuesta y Django puede enviarla al navegador del usuario.

Por supuesto, la descripción anterior está sumamente simplificada, pero no necesitas saber todas las cosas técnicas _aun_. Tener una idea general es suficiente.

Así que en lugar de meternos demasiado en los detalles, comenzaremos creando algo con Django y aprenderemos todas las piezas importantes en el camino.
