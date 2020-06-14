# SW API GraphQL

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project
```
git clone https://github.com/gustav0/swapi.git
```

Move into de repo and install dependencies
```
pip install -r requirements.txt
```

Create a .env file with a secret key or [get one](https://djecrety.ir/) manually and set it in the settings.py
```
python -c 'from django.core.management.utils import get_random_secret_key; print("SECRET_KEY={}".format(get_random_secret_key()))' > swapi/.env
```


Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```
Now the project is all set.

### Running the server
```
python manage.py runserver
```

### Runing the tests
```
python manage.py test
```

## Extras
Agregué un collection de postman dentro del directorio `extra` del repositorio, el cual contiene todos los request ya armados para hacer pruebas (le quité todas las variables del environment para que no tengan que crear nada, si se me pasó alguna me disculpo).

## Notas
(Perdón por el spanglish.)
1. Creo que cumplí con todas las consideraciones, pero tengo una observación con los unittests:
 - Solo realicé tests para `People` por temas de tiempo.
 - Utilicé un id fijo en el código para verificar la respuesta de creación y realizar la prueba de update. (Aún no estoy seguro cómo funcionan los ids generados por graphene-django por lo que es posible que no funcionen los unittest en otro ambiente diferente al mío).
 - En caso de que falle el comando para tests muy probablemente la causa sea lo que menciono en el punto anterior. El offending code sería este id: `UGVvcGxlTm9kZTo4OQ==` en `app/tests.py`
2. No alcancé a implementar sistemas de autenticación. Sin embargo he utilizado diferentes librebrías que abarcan varios casos de uso como:
 - [Django OAuth Toolkit](https://github.com/jazzband/django-oauth-toolkit) - Para trabajar con proveedores externos.
 - [Simple JWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt) - Para trabajar con credenciales de usuarios.
 - O simplemente usar BasicAuth o SessionAuth de Django.
 3. Con respecto a documentación especifica para GraphQL honestamente les digo que no tengo ni la menor idea de cuales son los estándares ni la forma apropiada de generar, organizar y mantener la documentación. Pero trabajo continuamente con swagger siguiendo el OpenAPI en proyectos con API Rest.
 4. Con respecto a "Testing avanzado" imagino que se refieren a librerías especializadas en testing como [pytest](https://github.com/pytest-dev/pytest/), análisis de covertura de código, e implementación de CI. Podría hacer algo pero no tengo suficiente base ni experiencia en testing de GraphQL como para decidir que librería se adapta mejor ni creer que la covertura sería asertada y un CI sería overkill.
