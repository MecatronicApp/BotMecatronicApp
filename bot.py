from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import sys

# Preguntas frecuentes actualizadas
FAQ = {
    "Links de Prácticas Libres": "Aquí tienes el enlace al formulario: https://docs.google.com/forms/d/e/1FAIpQLSeDIdpoZFaWkOJAZNzz4uuVCC1TX5LbRSSwhPbhY3xdWH6e-w/viewform",
    "Inicio de seminarios": "Los seminarios empiezan la semana del 12 de febrero.",
    "Horario general": "Puedes consultar el horario general en el grupo de Telegram oficial.",
    "Otra duda": "Por favor consulta con el coordinador o envía un correo a info@mechatronica.edu"
}

# Teclado personalizado actualizado
menu_opciones = [["Links de Prácticas Libres"], ["Inicio de seminarios"], ["Horario general"], ["Otra duda"]]
teclado = ReplyKeyboardMarkup(menu_opciones, one_time_keyboard=True, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy el Asistente Mecatrónico 🤖\n¿Cómo estás?",
        reply_markup=teclado
    )

# mensajes
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto in FAQ:
        await update.message.reply_text(FAQ[texto])
    else:
        await update.message.reply_text("No entiendo tu mensaje 😅. Elige una opción del menú o escribe /start para comenzar.")

# EJECUTAR
def main():
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = Application.builder().token("7521983171:AAFykiXcgVA1UBjT8B6ghtnQz_FvWyN_lQM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot en marcha...")
    app.run_polling()

if __name__ == '__main__':
    main()
