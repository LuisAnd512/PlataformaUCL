# Proyecto Django con AdminKit Template

Este repositorio contiene un proyecto Django que utiliza la plantilla HTML de [AdminKit](https://themewagon.com/themes/free-exciting-bootstrap-5-html5-ui-kits-template-adminkit/)  (versión libre 3.1.0) para crear un sitio web con una página de inicio (landing page) y una interfaz de administración. La siguiente guía te ayudará a configurar y ejecutar el proyecto en un entorno virtual.

## Requisitos Previos

Asegúrate de tener instalados los siguientes requisitos antes de comenzar:

- Python 3.x
- Virtualenv (opcional pero altamente recomendado)

## Configuración del Entorno Virtual

1. Clona el repositorio:

```bash
git clone <url_del_repositorio>
cd <nombre_del_repositorio>
```

2. Crea un entorno virtual (opcional pero recomendado):


```bash
virtualenv venv
```

3. Activa el entorno virtual:

- En Windows:
```bash
.\venv\Scripts\activate
```

- En Linux/Mac:
``` bash
source venv/bin/activate
```

4. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Configuración del Proyecto Django

1. Realiza las migraciones de la base de datos:

```bash
python manage.py migrate
```

2. Crea un superusuario para acceder a la interfaz de administración:

```bash
python manage.py createsuperuser
```

3. Sigue las instrucciones para crear un nombre de usuario, correo electrónico y contraseña.

## Ejecución del Proyecto

1. Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

2. Abre tu navegador y accede a http://127.0.0.1:8000/ para ver la página de inicio.

3. Accede a http://127.0.0.1:8000/admin/ e inicia sesión con las credenciales del superusuario para acceder a la interfaz de administración.

## Personalización y Desarrollo Adicional

Puedes personalizar la plantilla HTML en la carpeta `template` según las necesidades de tu proyecto.
Agrega y modifica las aplicaciones de Django en el directorio `apps`.
Explora y ajusta la configuración del proyecto en `settings.py` según tus requisitos específicos.

## Problemas Comunes

Si encuentras algún problema con las dependencias, verifica que estás utilizando el entorno virtual correctamente.
Asegúrate de haber aplicado las migraciones y creado el superusuario antes de acceder a la interfaz de administración.
¡Disfruta desarrollando tu proyecto con Django y la plantilla AdminKit! Si tienes alguna pregunta o problema, no dudes en abrir un problema en el repositorio o buscar ayuda en la documentación de Django y AdminKit.

## Licencias

### Template HTML (Adminkit)

El template HTML Adminkit Free esta distribuido por [ThemeWagon](https://themewagon.com/) y su uso esta dado según sus políticas de [licenciamiento](https://themewagon.com/license/) en su versión libre.

### Adaptación para Django

Este proyecto, incluyendo la adaptación del template HTML para Django, está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
