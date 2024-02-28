# tcjexl

Recubrimiento de la librería de [pyjexl](https://pypi.org/project/pyjexl/) incluyendo un conjunto de transformaciones por defecto (detalladas [en esta lista](#funciones-incluida))

Ejemplo de uso:

```python
from tcjexl import JEXL

jexl = JEXL()

context = {"a": 5, "b": 7, "c": "a TEXT String"}

print(jexl.evaluate('a+b', context))
print(jexl.evaluate('c|lowercase', context))
```

Resultado:

```
12
a text string
```

## Funciones incluidas

* `lowercase`: Transformación que nos convierte un string a lowercase

## Changelog
