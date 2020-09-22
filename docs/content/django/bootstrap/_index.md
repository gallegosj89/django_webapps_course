---
title: CSS
weight: 6
---

Nuestro blog todavía se ve bastante feo, es hora de hacerlo apreciable a la vista. Vamos a usar CSS para eso.

## Cascading Style Sheets

Cascading Style Sheets (CSS), que significa 'hojas de estilo en cascada'. Es un lenguaje utilizado para describir el aspecto y el formato de un sitio web escrito en lenguaje de marcado (como HTML). Es como maquillaje para páginas web.

Pero no queremos empezar de cero y diseñar todos los iconos, imágenes, tipografías, etc. Una vez más, usaremos algo que ya ha sido realizado por programadores y publicado en Internet de forma gratuita. Ya sabes, debemos de utilizar todas las herramientas disponibles y no reinventar la rueda.

## Usando Bootstrap

Bootstrap es uno de los frameworks HTML y CSS más populares para desarrollar webs agradables al ojo: <https://getbootstrap.com/>

Lo escribieron programadores que trabajaban para Twitter y ahora lo desarrollan voluntarios de todo el mundo.

### Instalar Bootstrap

Para instalar Bootstrap tienes que añadir esto al `<head>` de tu fichero `.html` (`blog/templates/blog/post_list.html`):

```html
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
```

Esto no añade ningún fichero a tu proyecto. Simplemente apunta a ficheros que existen en Internet. Adelante, abre tu sitio web y actualiza la página. Aquí está:

![1301-bootstrap1](/images/1301-bootstrap1.png)

Se ve mucho mejor.

## Ficheros estáticos en Django

Finalmente nos vamos a fijar en estas cosas que hemos estado llamando **ficheros estáticos**. Los ficheros estáticos son todos tus CSS e imágenes; ficheros que no son dinámicos, por lo que su contenido no depende del contexto de la petición y serán iguales para todos los usuarios.

### Dónde poner los ficheros estáticos para Django

Django ya sabe donde encontrar los ficheros estáticos para la aplicación "admin". Ahora necesitamos agregar algunos ficheros para nuestra aplicación, `blog`.

```bash
django-daw
├── blog
│   ├── migrations
|   ├── static
│   └── templates
└── mysite
```

Django encontrará automáticamente cualquier carpeta que se llame "static" dentro de las carpetas de tus aplicaciones. Entonces podrá utilizar su contenido como ficheros estáticos.

## Tu primer fichero CSS

Crea un nuevo directorio llamado `css` dentro de tu directorio `static`. Para añadir tu propio estilo a tu página web, crea un nuevo fichero llamado `blog.css` dentro de este directorio `css`.

```bash
django-daw
└─── blog
        └─── static
            └─── css
                └─── blog.css
```

Es hora de escribir algo de CSS. Abre el fichero `blog/static/css/blog.css` en tu editor de código.

No vamos a entrar mucho en la personalización y el aprendizaje de CSS aquí porque es bastante fácil y lo puedes aprender por tu cuenta después de está práctica. Recomiendo enormemente hacer este [curso de HTML y CSS en Codecademy](https://www.codecademy.com/tracks/web) para aprender todo lo que necesitas saber sobre cómo hacer tus sitios web más bonitos con CSS.

Pero vamos a hacer un poco al menos. ¿Tal vez podríamos cambiar el color de nuestro título? Los ordenadores utilizan códigos especiales (hexadecimal) para entender los colores. Empiezan con `#` y les siguen 6 letras (A-F) y números (0-9). Puedes encontrar códigos de color, por ejemplo, aquí: <http://www.colorpicker.com/>. También puedes utilizar [colores predefinidos](http://www.w3schools.com/cssref/css_colornames.asp) utilizando su nombre en inglés, como `red` y `green`.

En tu fichero `blog/static/css/blog.css` deberías añadir el siguiente código:

```css
h1 a,
h2 a {
    color: #c25100;
}
```

`h1 a` es un selector CSS. Quiere decir que estamos aplicando nuestros estilos a cualquier elemento `a` que se encuentre dentro de un elemento `h1`; el selector `h2 a` hace lo mismo para los elementos `h2` (por ejemplo cuando tenemos en código algo como: `<h1><a href="">enlace</a></h1>`). En este caso le estamos diciendo que cambie el color a `#C25100`, que es naranja. Puedes poner el color de tu elección aquí, asegurate de que haga buen contraste con el fondo blanco.

En un fichero CSS definimos los estilos para los elementos del fichero HTML. Los elementos se identifican por el nombre del elemento (es decir, `a`, `h1`, `body`), el atributo `class` (clase) o el atributo `id` (identificador). Class e id son nombres que le asignas tú mismo al elemento. Las clases definen grupos de elementos y los ids apuntan a elementos específicos. Por ejemplo, la siguiente etiqueta se puede identificar con CSS usando el nombre `a`, la clase `external_link` o el id `link_to_wiki_page`:

```html
<a href="https://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page"></a>
```

Puedes leer más sobre [selectores de CSS en w3schools](http://www.w3schools.com/cssref/css_selectors.asp).

También necesitamos decirle a nuestra plantilla HTML que hemos añadido CSS. Abre el fichero `blog/templates/blog/post_list.html` y añade esta línea justo al principio:

```html
{% load static %}
```

Aquí sólo estamos cargando ficheros estáticos. Luego, entre el `<head>` y `</head>`, después de los enlaces a los ficheros CSS de Bootstrap (el navegador lee los ficheros en el orden en que están, así que nuestro fichero podría sobrescribir partes del código de Bootstrap), añade la siguiente línea:

```html
<link rel="stylesheet" href="{% static 'css/blog.css' %}" />
```

El navegador lee los archivos en el orden en el que se le dan, así que tenemos que asegurarnos que este es el lugar correcto. De otra manera el código en nuestro archivo sera sobre escrito por los archivos de Bootstrap. Justo le decimos a nuestra plantilla donde esta localizado nuestro fichero CSS.

Ahora tu fichero debería tener este aspecto:

```html
{% load static %}
<html>
    <head>
        <title>Django Daw blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
        <link rel="stylesheet" href="{% static 'css/blog.css' %}" />
    </head>
    <body>
        <div>
            <h1><a href="/">Django Daw Blog</a></h1>
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

De acuerdo, guarda el fichero y actualiza el sitio.

![1302-color2](/images/1302-color2.png)

Demos un poco de aire a nuestro sitio web y aumentemos también el margen en el lado izquierdo:

```css
body {
    padding-left: 15px;
}
```

Añade esto a tu CSS, guarda el fichero y mira cómo funciona.

![1303-margin2](/images/1303-margin2.png)

Personaliza la tipografía del título, pega esto en la sección `<head>` del fichero `blog/templates/blog/post_list.html`:

```html
<link href="https://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css" />
```

Así como antes, verifica el orden y colocala justo antes del enlace a `blog/static/css/blog.css`. Esta línea va a importar una tipografía llamada _Lobster_ de Google Fonts (<https://www.google.com/fonts>).

Ahora añade la línea `font-family: 'Lobster';` en el fichero CSS `blog/static/css/blog.css` dentro del bloque de declaración `h1 a` (el código entre llaves `{` y `}`) y actualiza la página:

```css
h1 a,
h2 a {
    color: #c25100;
    font-family: "Lobster";
}
```

![1304-font](/images/1304-font.png)

Como se mencionó anteriormente, CSS tiene un concepto de clases que básicamente permite nombrar una parte del código HTML y aplicar estilos sólo a esta parte, sin afectar a otras. Es muy útil si tienes dos divs que hacen algo muy diferente (como el encabezado y la entrada) y no quieres que tengan el mismo aspecto.

Nombra algunas partes del código HTML. Añade una clase llamada `page-header` al `div` que contiene el encabezado, así:

```html
<div class="page-header">
    <h1><a href="/">Django Daw Blog</a></h1>
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

Ahora añadiremos bloques de declaración a diferentes selectores. Los selectores que comienzan con `.` hacen referencia a las clases. Hay muchos tutoriales y explicaciones sobre CSS en la web que te ayudarán a entender el siguiente código. Por ahora, simplemente copia y pega este bloque de código en tu fichero `blog/static/css/blog.css`:

```css
.page-header {
    background-color: #c25100;
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
    font-family: "Lobster", cursive;
}

.date {
    color: #828282;
}

.save {
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

Guarda los ficheros y actualiza tu sitio.

![1305-final](/images/1305-final.png)

Bien!, se ve mucho mejor. En realidad el código que acabamos de pegar no es tan difícil de entender y deberías ser capaz de entender la mayoría sólo con leerlo.

No tengas miedo de jugar un poco con este CSS e intentar cambiar algunas cosas. Si rompes algo, no te preocupes, siempre puedes deshacerlo.

De cualquier forma, te vuelvo a recomendar que hagas el [curso de HTML y CSS de Codeacademy](https://www.codecademy.com/tracks/web) como una tarea post-clase para que aprendas todo lo que necesitas saber para hacer tus sitios web más bonitos con CSS.
