
# Plantilla de servidor web minimalista con flask
## Obtener el código
- Descargaremos la carpeta con el código necesario para crear nuestro servidor local.

            git clone https://github.com/jorfernan/server.git

## Acceder a la carpeta
- **[IMPORTANTE]** Una vez descargada la carpeta, accedemosa la misma y ejecutamos Visual Studio Code en ella para tenerla como directorio raiz. 
- Linux
            cd server && code .

- Windows

            cd server ; code .

## Instalar el interprete de python (Windows)

- En Windows

            - Abrir un terminal e insertar el comando python, luego, instalarlo desde la tienda de Windows 

            - https://www.python.org/downloads/

- En Linux

            sudo apt update && sudo apt install python3 python3-venv python3-pip -y

## Entorno virtual 
- En Linux: **No utilizar sudo** para ninguno de los siguientes comandos

            python3 -m venv venv

- En Windows

            python -m venv venv

## Activación entorno virtual
Depende del SO. Accede a la carpeta venv y localiza el script de activación del entorno virtual.

- Linux

            source venv/bin/activate

- Windows

            .\venv\Scripts\activate

Debería aparecer en la terminal de VS Code lo siguiente antes de cada comando **(venv)**

## Instalación de dependencias
Las dependencias son todos aquellos fragmentos de código de terceros que utilizaremos para crear nuestro servidor.
- En windows

            pip install -r requirements.txt

- En Linux

            pip3 install -r requirements.txt


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
- Abrir un navegador y acceder a la siguiente URL

            htttp://localhost:5000