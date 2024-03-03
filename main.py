import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from binance.client import Client
import aiohttp
import asyncio
from apikey import api_key, bot_token

CMC_API_KEY = api_key
BOT_TOKEN = bot_token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# Función para obtener el precio del Bitcoin en CLP
async def check_clp_price():
    # Se crea una sesión de aiohttp para realizar la petición a la API
    async with aiohttp.ClientSession() as session:
        api_key = CMC_API_KEY
        headers = {'X-CMC_PRO_API_KEY': api_key, 'Accept': 'application/json'}
        url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
        params = {'amount': 1, 'symbol': 'BTC', 'convert': 'CLP'}

        async with session.get(url, headers=headers, params=params) as response:
            if response.status == 200:
                data = await response.json()
                # Extracción del precio de BTC en CLP desde la respuesta de la API
                precio_btc_clp = data['data'][0]['quote']['CLP']['price']
                return precio_btc_clp
            else:
                error_message = await response.text()
                raise Exception(f"Error en la respuesta de la API: {response.status} - {error_message}")

# Función para obtener el precio del Bitcoin en USD
async def check_btc_price():
    # Se crea una sesión de aiohttp para realizar la petición a la API
    async with aiohttp.ClientSession() as session:
        api_key = CMC_API_KEY
        headers = {'X-CMC_PRO_API_KEY': api_key, 'Accept': 'application/json'}
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        params = {'symbol': 'BTC'}

        async with session.get(url, headers=headers, params=params) as response:
            if response.status == 200:
                data = await response.json()
                # Extracción del precio de BTC en USD desde la respuesta de la API
                precio_btc_usd = data['data']['BTC']['quote']['USD']['price']
                return precio_btc_usd
            else:
                error_message = await response.text()
                raise Exception(f"Error en la respuesta de la API: {response.status} - {error_message}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=update.message.text
    )

# Funcion para enviar el precio del Bitcoin en USD y CLP
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio_btc_usd = await check_btc_price()
        precio_btc_clp = await check_clp_price()
        message = f"El precio actual de BTC en CLP es de {precio_btc_clp:.1f} CLP. El precio actual de BTC en USD es de {precio_btc_usd:.1f} USD."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))

# Función para enviar el precio del Bitcoin cada 15 minutos en USD y CLP automáticamente
auto_check_price = False

async def autoCheckPrice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global auto_check_price  # Add this line to access the global variable
    auto_check_price = True
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Se ha iniciado la verificación automática de precios."
    )
    while auto_check_price:
        try:
            precio_btc_usd = await check_btc_price()
            precio_btc_clp = await check_clp_price()
            message = f"{precio_btc_usd:.1f} USD / \n{precio_btc_clp:.1f} CLP"
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=message
            )
        except Exception as e:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f'Hubo un problema al acceder a los datos de la API: {e}'
            )
        await asyncio.sleep(15)  # Espera de manera asíncrona 15 segundos

async def stopAutoCheckPrice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global auto_check_price  # Add this line to access the global variable
    auto_check_price = False
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Se ha detenido la verificación automática de precios."
    )
    return

if __name__ == '__main__':

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    price_handler = CommandHandler('price', price)
    autoCheckPrice_handler = CommandHandler('autoprice', autoCheckPrice)
    stopAutoCheckPrice_handler = CommandHandler('stopprice', stopAutoCheckPrice)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(price_handler)
    application.add_handler(autoCheckPrice_handler)
    application.add_handler(stopAutoCheckPrice_handler)

    application.run_polling()