from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import sys

# Preguntas frecuentes
FAQ = {
    "QRs de Practical Libre": "Los QRs se publican cada lunes en el aula Moodle de la materia.",
    "Inicio de seminarios": "Los seminarios empiezan la semana del 12 de febrero.",
    "Horario general": "Puedes consultar el horario general en el grupo de Telegram oficial.",
    "Otra duda": "Por favor consulta con el coordinador o envía un correo a info@mechatronica.edu"
}

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy el Asistente Mecatrónico 🤖\n¿Cómo estás?")

# mensajes
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "hola" in texto or "bien" in texto or "buenos" in texto:
        menu_texto = (
            "Genial 😄 ¿Qué quieres saber?\n\n"
            "1️⃣ QRs de Practical Libre\n"
            "2️⃣ Inicio de seminarios\n"
            "3️⃣ Horario general\n"
            "4️⃣ Otra duda"
        )
        await update.message.reply_text(menu_texto)
    elif update.message.text in FAQ:
        await update.message.reply_text(FAQ[update.message.text])
    else:
        await update.message.reply_text("No entiendo tu mensaje 😅. Elige una opción del menú o escribe /start para comenzar.")

# EJECUTAR
def main():
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = Application.builder().token("TU_TOKEN_AQUI").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot en marcha...")
    app.run_polling()

if __name__ == '__main__':
    main()
