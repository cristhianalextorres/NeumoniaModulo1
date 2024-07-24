# NeumoniaModulo1
Micro proyecto del modulo uno : Desarrollo de proyectos IA

En el presente proyecto se despliega una aplicación que detecta tres tipos de Neumonía. Para ejecutar el proyecto se deben seguir los siguientes pasos:

**1. Descargar el repositorio**
Todos los archivos de este repositorio deben quedar en la misma carpeta. También debe quedar el modelo preentrenado que se encunetra en el siguiente link:

**2. Construción del Contenedor con Docker:**

Se recomienda usar la siguiente instrucción para crear el contenedor:

docker build -t <Nombre_Contenedor>

**3. Correr Contenedor:**

Se sugiere correr el contenedor con la siguinete instrucción y referenciar al contenedor por ID:

docker run -it -e DISPLAY=host.docker.internal:0.0 <ID_Contenedor>

**4. Ejecutar Aplicación:**

Desde Docker Desktop, se ingresa al contenedor con estado Running y en la pestaña "Exec" se inicia la aplicación con el siguiente comando:
python3 main.py

Con ayuda de Xming se debe desplegar la ventana de la aplicación.

**5. Selección Imagenes de prueba**
En la ventana de la aplicación, en el boton cargar, se despliega el buscador de archivos, se debe ingresar a:

home -> src

En esa ubicación estan los archivos de prueba.

# Muchas gracias por su atención




