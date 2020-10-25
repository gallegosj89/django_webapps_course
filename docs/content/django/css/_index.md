---
title: CSS
weight: 6
---

Nuestro blog todavía se ve bastante feo, es hora de hacerlo apreciable a la vista. Vamos a usar CSS para eso.

## Cascading Style Sheets

Cascading Style Sheets (CSS), que significa 'hojas de estilo en cascada'. Es un lenguaje utilizado para describir el aspecto y el formato de un sitio web escrito en lenguaje de marcado (como HTML). Es como maquillaje para páginas web.

Pero no queremos empezar de cero y diseñar todos los iconos, imágenes, tipografías, etc. Una vez más, usaremos algo que ya ha sido realizado por programadores y publicado en Internet de forma gratuita. Ya sabes, debemos de utilizar todas las herramientas disponibles y no reinventar la rueda.

### Bootstrap

Bootstrap es uno de los frameworks CSS más populares para desarrollar webs agradables a la vista, pueds encontrar más ionformación en [la web oficial](https://getbootstrap.com/)

Este framework fue escrito por desarrolladores que trabajaban para Twitter y ahora lo continúan manteniendo voluntarios de todo el mundo, por lo que es un proyecto de código libre.

### Usando Bootstrap

Para instalar Bootstrap tienes que añadir esto al `<head>` de tu archivo `.html` (`blog/templates/blog/post_list.html`):

```html
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
```

Esto no añade ningún archivo a tu proyecto. Simplemente apunta a archivos que existen en Internet. Adelante, abre tu sitio web y actualiza la página. Aquí está:

![css-bootstrap.png](css-bootstrap.png?height=350px)

Se ve mucho mejor.

## Archivos estáticos en Django

Finalmente nos vamos a fijar en estas cosas que hemos estado llamando **archivos estáticos**. Los archivos estáticos son todos tus CSS e imágenes; archivos que no son dinámicos, por lo que su contenido no depende del contexto de la petición y serán iguales para todos los usuarios.

### Dónde poner los recursos estáticos para Django

Django ya sabe donde encontrar los archivos estáticos para la aplicación "admin". Ahora necesitamos agregar algunos archivos para nuestra aplicación, `blog`.

```bash
django-daw
├── blog
│   ├── migrations
|   ├── static
│   └── templates
└── mysite
```

Django encontrará automáticamente cualquier carpeta que se llame "static" dentro de las carpetas de tus aplicaciones. Entonces podrá utilizar su contenido como archivos estáticos.

### Tu primer archivo CSS

Crea un nuevo directorio llamado `css` dentro de tu directorio `static`. Para añadir tu propio estilo a tu página web, crea un nuevo archivo llamado `blog.css` dentro de este directorio `css`.

```bash
django-daw
└─── blog
        └─── static
            └─── css
                └─── blog.css
```

Es hora de escribir algo de CSS. Abre el archivo `blog/static/css/blog.css` en tu editor de código.

No vamos a entrar mucho en la personalización y el aprendizaje de CSS aquí porque es bastante fácil y lo puedes aprender por tu cuenta después de está práctica. Recomiendo enormemente hacer este [curso de HTML y CSS en Codecademy](https://www.codecademy.com/tracks/web) para aprender todo lo que necesitas saber más sobre darle una mejor presentación a tus páginas web.

Pero al menos agreguemos un poco de diseño institucional al blog. ¿Tal vez podríamos cambiar el color de nuestro título? Nuestra computadora utiliza códigos especiales (hexadecimal) para entender los colores. Estos códigos en CCS empiezan con `#` y les siguen 6 letras (A-F) y/o números (0-9). Puedes encontrar códigos de color, por ejemplo [en esta web](http://www.colorpicker.com/). También puedes utilizar [colores predefinidos](http://www.w3schools.com/cssref/css_colornames.asp) utilizando su nombre en inglés, como `red` y `green`.

En tu archivo `blog/static/css/blog.css` deberías añadir el siguiente código:

```css
h1 a,
h2 a {
    color: #00723f;
}
```

`h1 a` es un selector CSS. Quiere decir que estamos aplicando nuestros estilos a cualquier elemento `a` que se encuentre dentro de un elemento `h1`; el selector `h2 a` hace lo mismo para los elementos `h2` (por ejemplo cuando tenemos en código algo como: `<h1><a href="">enlace</a></h1>`). En este caso le estamos diciendo que cambie el color a `#00723F`, que es el verde institucional. Puedes poner el color de tu elección aquí, asegurate de que haga buen contraste con el fondo blanco.

En un archivo CSS definimos los estilos para los elementos del archivo HTML. Los elementos se identifican por el nombre del elemento (es decir, `a`, `h1`, `body`), el atributo `class` (clase) o el atributo `id` (identificador). Class e id son nombres que le asignas tú mismo al elemento. Las clases definen grupos de elementos y los ids apuntan a elementos específicos. Por ejemplo, la siguiente etiqueta se puede identificar con CSS usando el nombre `a`, la clase `external_link` o el id `link_to_wiki_page`:

```html
<a href="https://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page"></a>
```

Puedes leer más sobre [selectores de CSS en w3schools](http://www.w3schools.com/cssref/css_selectors.asp).

También necesitamos decirle a nuestra plantilla HTML que hemos añadido CSS. Abre el archivo `blog/templates/blog/post_list.html` y añade esta línea justo al principio:

```html
{% load static %}
```

Aquí sólo estamos cargando archivos estáticos. Luego, entre el `<head>` y `</head>`, después de los enlaces a los archivos CSS de Bootstrap (el navegador lee los archivos en el orden en que están, así que nuestro archivo podría sobrescribir partes del código de Bootstrap), añade la siguiente línea:

```html
<link rel="stylesheet" href="{% static 'css/blog.css' %}" />
```

El navegador lee los archivos en el orden en el que se le dan, así que tenemos que asegurarnos que este es el lugar correcto. De otra manera el código en nuestro archivo sera sobre escrito por los archivos de Bootstrap. Justo le decimos a nuestra plantilla donde esta localizado nuestro archivo CSS.

Ahora tu archivo debería tener este aspecto:

```html
{% load static %}
<html>
    <head>
        <title>DAW blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
        <link rel="stylesheet" href="{% static 'css/blog.css' %}" />
    </head>
    <body>
        <div>
            <h1><a href="/">DAW Blog</a></h1>
        </div>

        {% for post in posts %}
        <div>
            <p>publicado: {{ post.published_date }}</p>
            <h2><a href="">{{ post.title }}</a></h2>
            <p>{{ post.text|linebreaksbr }}</p>
        </div>
        {% endfor %}
    </body>
</html>
```

De acuerdo, guarda el archivo y actualiza el sitio.

![css-headers.png](css-headers.png?height=350px)

Demos un poco de aire a nuestro sitio web y aumentemos también el margen en el lado izquierdo:

```css
body {
    padding-left: 15px;
}
```

Añade esto a tu CSS, guarda el archivo y mira cómo funciona.

![css-body_padding.png](css-body_padding.png?height=350px)

Personaliza la tipografía del título, pega esto en la sección `<head>` del archivo `blog/templates/blog/post_list.html`:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Text:wght@600&display=swap" />
```

Así como antes, verifica el orden y colocala justo antes del enlace a `blog/static/css/blog.css`. Esta línea va a importar una tipografía llamada _Crimson Text_ de [la API de Google](https://www.google.com/fonts).

{{%notice tip%}}
**Tip**
\
Si deseas utilizar otra tipografía, puedes encontrar algunas gratuitas en el [servio de tipografías de Google](https://fonts.google.com/).
{{%/notice%}}

Ahora añade la línea `font-family: "Crimson Text";` en el archivo CSS `blog/static/css/blog.css` dentro del bloque de declaración `h1 a` (el código entre llaves `{` y `}`) y actualiza la página:

```css
h1 a,
h2 a {
    color: #00723f;
    font-family: "Crimson Text";
}
```

![css-font.png](css-font.png?height=350px)

Como se mencionó anteriormente, CSS tiene un concepto de clases que básicamente permite nombrar una parte del código HTML y aplicar estilos sólo a esta parte, sin afectar a otras. Es muy útil si tienes dos divs que hacen algo muy diferente (como el encabezado y la entrada) y no quieres que tengan el mismo aspecto.

Nombra algunas partes del código HTML. Añade una clase llamada `page-header` al `div` que contiene el encabezado, así:

```html
<div class="page-header">
    <h1><a href="/">DAW Blog</a></h1>
</div>
```

Y ahora añade la clase `post` al `div` que contiene una entrada del blog.

```html
<div class="post">
    <p>publicado: {{ post.published_date }}</p>
    <h2><a href="">{{ post.title }}</a></h2>
    <p>{{ post.text|linebreaksbr }}</p>
</div>
```

Ahora añadiremos bloques de declaración a diferentes selectores. Los selectores que comienzan con `.` hacen referencia a las clases. Hay muchos tutoriales y explicaciones sobre CSS en la web que te ayudarán a entender el siguiente código. Por ahora, simplemente copia y pega este bloque de código en tu archivo `blog/static/css/blog.css`:

```css
.page-header {
    background-color: #00723f;
    margin-top: 0;
    padding: 20px 20px 20px 40px;
}

.page-header h1,
.page-header h1 a,
.page-header h1 a:visited,
.page-header h1 a:active {
    color: #ffffff;
    font-size: 36pt;
    text-decoration: none;
}

.content {
    margin-left: 40px;
}

h1,
h2,
h3,
h4 {
    font-family: "Crimson Text";
}

.date {
    float: right;
    color: #828282;
}

.pull-right {
    float: right;
}

.post-form textarea,
.post-form input {
    width: 100%;
}

.top-menu,
.top-menu:hover,
.top-menu:visited {
    color: #ffffff;
    float: right;
    font-size: 26pt;
    margin-right: 20px;
}

.post {
    margin-bottom: 70px;
}

.post h1 a,
.post h1 a:visited,
.post h2 a,
.post h2 a:visited {
    color: #000000;
}
```

Luego rodea el código HTML que muestra las entradas con las declaraciones de clases. Sustituye esto:

```html
{% for post in posts %}
<div class="post">
    <p>publicado: {{ post.published_date }}</p>
    <h2><a href="">{{ post.title }}</a></h2>
    <p>{{ post.text|linebreaksbr }}</p>
</div>
{% endfor %}
```

en `blog/templates/blog/post_list.html` por esto:

```html
<div class="content container">
    <div class="row">
        <div class="col-md-8">
            {% for post in posts %}
            <div class="post">
                <div class="date">
                    <p>publicado: {{ post.published_date }}</p>
                </div>
                <h2><a href="">{{ post.title }}</a></h2>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
```

Guarda los archivos y actualiza tu sitio.

![css-final.png](css-final.png?height=450px)

Bien!, se ve mucho mejor. En realidad el código que acabamos de pegar no es tan difícil de entender y deberías ser capaz de entender la mayoría sólo con leerlo.

No tengas miedo de jugar un poco con este CSS e intentar cambiar algunas cosas. Si rompes algo, no te preocupes, siempre puedes deshacerlo.

De verdad te recomiendo que hagas algunos cursos gratuitos como por ejemplo ["Basic HTML & HTML5"](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/) y ["Basic CSS"](https://www.freecodecamp.org/learn/responsive-web-design/basic-css/) de [freeCodeCamp](https://learn.freecodecamp.org/).

### Un archivo estático más

Por último vamos a añadir uno de los archivos estáticos más comunes de los sitios web, el conocido _favicon_. Seguro que lo conoces, solo que es muy posible que no por su nombre; si alguna vez has abierto una página web y en la pestaña aparece el icono del sitio al accedido, bueno pues ese icono es el _favicon_.

Este pequeñoicono le da mucha personalidad a una web, y hace que se vea un poco más presentable. Si haz seguido las instrucciones la pie de la letra, tu sitio tendrá como color principal el verde institucional - entonces descarga este [archivo de aquí](favicon.ico) y ponlo en el folder que creamos hace un momento `blog/static/` con el nombre `favicon.ico`.

{{%notice tip%}}
**Tip**
\
Si haz seleccionado un esquema de colores personalizado, o solo es que no te gusta el favicon de más arriba, [esta es una web](https://favicon.io/favicon-generator/) muy sencilla donde puedes crear el tuyo un poco más personalizado.
{{%/notice%}}

Ahora por último vamos a decir a nuestra plantilla que ligue el archivo cuando cree la página HTML. Solo agrega esta línea dentro de la etiqueta `head` de tu plantilla `post_list.html`.

```html
<link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
```

Por ejemplo:

```html
<head>
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Text:wght@600&display=swap" />
    <link rel="stylesheet" href="{% static 'css/blog.css' %}" />
    <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
    <title>DAW blog</title>
</head>
```
