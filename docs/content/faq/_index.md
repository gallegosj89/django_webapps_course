---
title: Frequently Asked Questions
weight: 60
alwaysopen: false
---

1. ¿Por qué el comando `python` no funciona en git bash?

Cuando se utiliza el comando `python` en la linea de comando de git bash podría suceder que se queda como si estuviera esperando algo. Si utilizas el mismo comando en CMD o Powershell, y efectivamente se abre el interprete de Python, entonces haz lo siguiente.

Abre una nueva ventana de git bash, crea un nuevo archivo llamado `.bashrc` en tu directorio HOME - para esto ejecuta el comando `touch ~/.bashrc`. Ahora edita ese archivo con Visual Studio Code (o el editor de tu preferencia) ejecutando `code ~/.bashrc`. Agrega lo siguiente:

```sh
alias python='winpty python.exe'
```

Cierra todas las ventanas de git bash, abre una nueva ventana de git bash y ejecuta el comando `python`. Deberia de abrirse el interprete de Python.
