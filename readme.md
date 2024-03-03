# BTC To CLP/USD UpdaterBOT

This is a Python-based Telegram bot that fetches and sends Bitcoin prices in USD and CLP. It uses the Coinmastercap API to fetch the prices.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.8 or higher installed on your machine. You also need to install the following Python libraries:

- `telegram`
- `aiohttp`

You can install them using pip:

```sh
pip install telegram aiohttp
```

### Installing

1. Clone the repository to your local machine.
2. Replace the placeholders in the [`apikey.py`](command:_github.copilot.openSymbolInFile?%5B%22apikey.py%22%2C%22apikey.py%22%5D "apikey.py") file with your Coinmastercap API key and Telegram bot token.

## Usage

Run the [`main.py`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22main.py%22%5D "main.py") script to start the bot:

```sh
python main.py
```

The bot supports the following commands:

- `/start`: Starts the bot.
- `/price`: Fetches and sends the current Bitcoin price in USD and CLP.
- `/autoprice`: Starts automatic price checking every 15 minutes.
- `/stopprice`: Stops automatic price checking.


## License

This project is licensed under the MIT License.

# ----------------------------------------------------------------

# BTC To CLP/USD UpdaterBOT

Este es un bot de Telegram basado en Python que obtiene y envía los precios de Bitcoin en USD y CLP. Utiliza la API de Coinmastercap para obtener los precios.

## Empezando

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para fines de desarrollo y pruebas.

### Prerrequisitos

Necesitas tener Python 3.8 o superior instalado en tu máquina. También necesitas instalar las siguientes librerías de Python:

- `telegram`
- `aiohttp`

Puedes instalarlas usando pip:

```sh
pip install telegram aiohttp
```

### Instalación

1. Clona el repositorio en tu máquina local.
2. Reemplaza los marcadores de posición en el archivo [`apikey.py`](command:_github.copilot.openSymbolInFile?%5B%22apikey.py%22%2C%22apikey.py%22%5D "apikey.py") con tu clave API de Coinmastercap y el token de tu bot de Telegram.

## Uso

Ejecuta el script [`main.py`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22main.py%22%5D "main.py") para iniciar el bot:

```sh
python main.py
```

El bot soporta los siguientes comandos:

- `/start`: Inicia el bot.
- `/price`: Obtiene y envía el precio actual de Bitcoin en USD y CLP.
- `/autoprice`: Inicia la comprobación automática de precios cada 15 minutos.
- `/stopprice`: Detiene la comprobación automática de precios.


## Licencia

Este proyecto está licenciado bajo la Licencia MIT
