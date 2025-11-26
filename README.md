
# Plantilla de servidor web minimalista con flask
## Obtener el código
git clone https://github.com/jorfernan/server.git

## Acceder a la carpeta
- Hago incapié en utilizar este comando para trabajar desde la carpeta de trabajo.
cd server

## Instalar el interprete de python (Windows)
- Abrir un terminal e insertar el comando python, luego, instalarlo desde la tienda de Windows 

## Entorno virtual 
- En linux: No utilizar sudo para ninguno de los siguientes comandos
python3 -m venv venv

- En windows
python -m venv venv

## Activación entorno virtual
Depende del SO. Accede a la carpeta venv y localiza el script de activación del entorno virtual.

- Linux
source venv/bin/activate

- Windows
.\venv\Scripts\activate

Debería aparecer en la terminal de VS Code lo siguiente antes de cada comando (venv)

## Instalación de dependencias
- En windows
pip install -r requirements.txt

- En Linux
pip3 install -r requirements.txt

Instalar pip3 si no está disponible en el SO

## Inicialización de la base de datos
- Windows
python init.py

- Linux
python3 init.py

## Inicializa el servidor
- Windows
python app.py

- Linux
python3 app.py

## Accede a la página
 htttp://localhost:5000