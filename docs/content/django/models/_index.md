---
title: Modelos
weight: 2
---

Lo que queremos crear ahora es algo que va a almacenar todos los posts en nuestro blog. Pero para poder hacerlo tenemos que hablar un poco acerca de algo llamado `objects`.

## Objetos

Hay un concepto en el mundo de la programación llamado programación orientada a objetos [`object-oriented programming`]. La idea es que en lugar de escribir todo como una secuencia de instrucciones de programación podemos modelar cosas y definir cómo interactúan con las demás.

Entonces ¿Qué es un objeto? Es un conjunto de propiedades y acciones. Como por ejemplo. Si queremos modelar un gato crearemos un objeto `Cat` que tiene algunas propiedades, como son por ejemplo `color`, `age`, `mood` (es decir, bueno, malo, sueño), `owner` (que es un objeto `Person` o, tal vez, en el caso de que el gato sea callejero, esta propiedad estará vacía).

Y luego el `Cat` tiene algunas acciones: `purr`, `scratch`, o `feed` (en la cual daremos al gato algunos `CatFood`, que podría ser un objeto independiente con propiedades, como por ejemplo, `taste`).

```text
Cat
--------
color
age
mood
owner
purr()
scratch()
feed(cat_food)

CatFood
----------
taste
```

Básicamente se trata de describir cosas reales en el código con propiedades (llamadas `object properties`) y las acciones (llamadas `methods`).

Queremos construir un blog, por lo que tenemos primero que responder algunas preguntas: ¿Qué es un post de un blog? ¿Qué características debe tener?

Seguro que nuestros posts necesitan un texto con su contenido y un título. También sería bueno saber quién lo escribió, así que necesitamos un autor. Por último, queremos saber cuándo el post fue creado y publicado.

```bash
Post
--------
title
text
author
created_date
published_date
```

¿Qué tipo de cosas podría hacerse con una entrada del blog? Sería bueno tener algún `method` que publique la entrada.

Así que vamos a necesitar el método `publish`. Puesto que ya sabemos lo que queremos lograr, podemos empezar a modelar en Django.

## Modelos en Django

Sabiendo qué es un objeto, podemos crear un modelo en Django para nuestros posts en el blog.

Un modelo en Django es un tipo especial de objeto que se guarda en la `database`. Una `database` es una colección de datos. Allí es el lugar en el cual almacenamos la información sobre usuarios, posts del blog, etc. Utilizaremos una base de datos SQLite para almacenar nuestros datos. Este es el adaptador de base de datos predeterminada en Django -- será suficiente para nosotros por ahora.

Piensa en el modelo en la base de datos como una hoja de cálculo con columnas (campos) y filas (datos).

## Creando una aplicación

Para mantener todo en orden, crearemos una aplicación separada dentro de nuestro proyecto. Es muy bueno tener todo organizado desde el principio. Para crear una aplicación, necesitamos ejecutar el siguiente comando en la consola.

{{%notice warning%}}
Recuerda entrar al directorio de tu proyecto, puedes llegar allí con `cd ~/django-daw` o `cd %userprofile%\django-daw`. Despues inicia el entorno virtual.
{{%/notice%}}

```bash
(env) $ python manage.py startapp blog
```

Vas a notar que se crea un nuevo directorio llamado `blog` y contiene una serie de archivos. Nuestros directorios y archivos en nuestro proyecto deberían verse así `tree . -L 2 -I env`:

```text
django-daw
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Después de crear una aplicación también necesitamos decirle a Django que debe utilizarla. Lo hacemos en el archivo `mysite/settings.py`. Tenemos que encontrar `INSTALLED_APPS` y añadir una línea que contenga `blog.apps.BlogConfig`, justo por encima del último `]`. El producto final debe tener este aspecto:

```python
INSTALLED_APPS = [
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
     'blog.apps.BlogConfig',
]
```

## Creando el modelo blog post

En el archivo `blog/models.py` definimos todos los objetos llamados `Models` - este es un lugar en el cual definiremos nuestro blog post. Vamos abrir `blog/models.py`, quitamos todo y escribimos un código como este:

```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

{{%notice info%}}
Vuelve a verificar que usaste dos guiones bajos (`_`) en cada lado del `str`. Esta convención se utilizan con frecuencia en Python y a veces también los llamamos "dunder" (diminutivo en inglés de "double-underscore").
{{%/notice%}}

Puede parecer un poco intimidante ese código, pero veamos qué significan estas líneas.

Todas las líneas que comienzan con `from` o `import` son líneas para añadir algo de otros archivos. Así que en vez de copiar y pegar las mismas cosas en cada archivo, podemos incluir algunas partes con `from... import ...`.

`class Post(models.Model):` - esta línea define nuestro modelo (es un `object`).

-   `class` es una palabra clave que indica que estamos definiendo un objeto.
-   `Post` es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Una clase siempre comienza con su primera letra en mayúscula.
-   `models.Model` significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.

Ahora definimos las propiedades que hablábamos: `title`, `text`, `created_date`, `published_date` y `author`. Para hacer eso tenemos que definir un tipo de campo (¿es texto? ¿un número? ¿una fecha? ¿una relación con otro objeto, como un usuario?).

-   `models.CharField` - así es como defines un texto con un número limitado de caracteres.
-   `models.TextField` - esto es para textos largos sin un límite. Será ideal para el contenido de un post, ¿verdad?
-   `models.DateTimeField` - esto es fecha y hora.
-   `modelos.ForeignKey` - este es un vínculo con otro modelo.

{{%notice info%}}
Si necesitas más información sobre los modelos de Django o quieres saber como trabajar con diferentes tipos de datos ve a la [documentación oficial](https://docs.djangoproject.com/en/3.1/topics/db/models/).
{{%/notice%}}

¿Y qué sobre `def publish(self):`? Es exactamente nuestro método `publish` que mencionamos anteriormente. `def` significa que se trata de una función/método y `publish` es el nombre del método. Puedes cambiarlo, si quieres. La regla es que usamos minúsculas y guiones bajos en lugar de espacios (es decir, si quieres tener un método que calcule el precio medio, este podría llamarse `calculate_average_price`).

Los métodos muy a menudo devuelven algo. Hay un ejemplo de esto en el método `__str__`. En este escenario, cuando llamamos a `__str__()` obtendremos un texto (**string**) con un título de Post.

Si algo todavía no está claro sobre modelos, ¡no dudes en preguntar!. Puede ser muy complicado, sobre todo cuando estás entendiendo qué son funciones y objetos mientras sigues este documento.

## Crear tablas para los modelos en tu `database`

El último paso es añadir nuestro nuevo modelo a nuestra base de datos. Primero tenemos que hacer que Django sepa que tenemos algunos cambios en nuestro modelo (acabamos de crearlo), escribe `python manage.py makemigrations blog`. Se verá así:

```bash
(env) $ python manage.py makemigrations blog
Migrations for 'blog':
    0001_initial.py:
    - Create model Post
```

{{%notice info%}}
Recuerda guardar los cambios de los archivos que modificaste. De otra manera, la computadora ejecutara la version anterior lo cual podría dar errores inesperados.
{{%/notice%}}

Django preparará un archivo de migración que tenemos que aplicar ahora a nuestra base de datos escribiendo `python manage.py migrate blog`. El resultado debe ser:

```bash
(env) $ python manage.py migrate blog
Operations to perform:
    Apply all migrations: blog
Running migrations:
    Applying blog.0001_initial... OK
```

Nuestro modelo de Post está ahora en nuestra base de datos.

## Administrador de Django

Para agregar, editar y borrar los posts que hemos modelado, utilizaremos el administrador de Django.

Vamos a abrir el archivo `blog/admin.py` y reemplazar su contenido con esto:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Como puedes ver, importamos (incluimos) el modelo Post definido en la práctica anterior. Para hacer nuestro modelo visible en la página del administrador, tenemos que registrar el modelo con `admin.site.register(Post)`.

De acuerdo, es hora de ver tu modelo Post. Recuerda ejecutar `python manage.py runserver` en la consola para correr el servidor web. Ve al navegador y teclea la dirección <http://localhost:8000/admin/>. Verás una página de ingreso como la que sigue:

![0701-login_page2](0701-login_page2.png)

Para poder ingresar deberás crear un _super-usuario_ - un usuario que tiene control sobre todo lo que hay en el sitio. Vuelve hacia atrás a tu línea de comandos (**ctrl+c**) y teclea `python manage.py createsuperuser`, presiona **Enter**.

{{%notice info%}}
Recuerda, para ejecutar nuevos comando mientras el servidor web esta corriendo, abre una nueva terminal y activa tu ambiente virtual.
{{%/notice%}}

Cuando sea necesario, teclea tu nombre de usuario (en minúsculas, sin espacios), dirección de e-mail y contraseña cuando sean requeridos. No te preocupes que no puedes ver tu contraseña mientras la tecleas - así es como debe ser. Simplemente escríbela y presiona **Enter** para continuar. La salida de este comando debería verse así (nombre de usuario y email deberían ser los tuyos):

```bash
(env) $ python manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```

Vuelve a tu navegador e ingresa con las credenciales de super usuario que elegiste, ahora deberías poder ver el panel de administración de Django.

![0702-django_admin3](0702-django_admin3.png)

Ve a _Posts_ y experimenta un poco con esto. Agrega cinco o seis posts del blog. No te preocupes por el contenido - puedes simplemente copiar y pegar texto de está práctica en el contenido de tus posts para ahorrar tiempo.

Asegúrate de que por lo menos dos o tres posts (pero no todos) tienen la fecha de publicación. Será útil luego.

![0703-edit_post3](0703-edit_post3.png)

{{%notice info%}}
Si quieres saber más sobre el administrador de Django, puedes visitar la [documentación de Django](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/).
{{%/notice%}}
