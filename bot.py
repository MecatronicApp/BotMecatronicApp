from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import sys

# Función para formatear respuestas
def formatear_respuesta(texto):
    return f"{texto}\n\n🔙 Volver al menú"

# Diccionario de preguntas frecuentes
FAQ = {
    "Links de Practicas Libres": formatear_respuesta("🔗 Puedes acceder a los links de Prácticas Libres desde aquí:\nhttps://docs.google.com/forms/d/e/1FAIpQLSeDIdpoZFaWkOJAZNzz4uuVCC1TX5LbRSSwhPbhY3xdWH6e-w/viewform"),
    
    "Fechas importantes": formatear_respuesta("📅 Aquí puedes consultar las fechas importantes del semestre:\nhttps://www.ecci.edu.co/cronograma-academico/"),
    
    "Como ver las calificaciones del corte": formatear_respuesta("📊 Puedes ver tus calificaciones ingresando a ARCA, sección 'Académico > Calificaciones'."),
    
    "Cuales son las fechas limites para dar de baja una clase": formatear_respuesta("📌 La fecha límite para dar de baja una clase sin beneficio económico es hasta la segunda semana del semestre."),
    
    "Donde realizar la evaluación de profesores": formatear_respuesta("📝 La ruta para la evaluación de docentes es:\nEvaluaciones institucionales > Evaluación estudiante ECCI"),
    
    "Como descargar el recibo de la matricula": formatear_respuesta("💳 Para descargar el recibo de matrícula ve a:\nCuenta financiera ➡️ Resumen facturas alumno ➡️ Selecciona el recibo ➡️ Generar recibo de pago"),
    
    "Precuniarios": formatear_respuesta("💰 Consulta los derechos pecuniarios aquí:\nwww.ecci.edu.co/derechos-pecuniarios/"),
    
    "Curso de Inglés": formatear_respuesta("📘 Información sobre los cursos de inglés:\nhttps://arca.ecci.edu.co/psc/arca_1/EMPLOYEE/SA/c/EC_FORM_MN.LC_CRL_FORMULARIO.GBL?&"),
    
    "Examen de Inglés": formatear_respuesta("🧪 Información sobre los exámenes de inglés:\nhttps://centrodelenguas.ecci.edu.co/examenes/"),
    
    "Correos importantes": formatear_respuesta(
        "✉️ Correos importantes:\n"
        "- financiera@ecci.edu.co\n"
        "- evaluame@ecci.edu.co\n"
        "- asistente.mecatronicabta@ecci.edu.co"
    ),
    
    "Aulas Virtuales": formatear_respuesta("🖥️ Accede a las Aulas Virtuales desde:\nhttps://aulas.ecci.edu.co"),
    
    "Ubicacion de las sedes": formatear_respuesta("📍 Consulta la ubicación de las sedes aquí:\nhttps://www.ecci.edu.co/bogota/directorio-de-sedes/?sede=5/")
}

# Menú principal con categorías
menu_categorias = [
    ["🎓 Académico", "🏛️ Administrativo"],
    ["💻 Plataformas", "📬 Contacto"]
]
teclado_categorias = ReplyKeyboardMarkup(menu_categorias, resize_keyboard=True)

# Submenús por categoría
submenu_academico = ReplyKeyboardMarkup([
    ["Links de Practicas Libres"],
    ["Fechas importantes"],
    ["Como ver las calificaciones del corte"],
    ["Cuales son las fechas limites para dar de baja una clase"],
    ["Cursos y Exámenes de Inglés"],
    ["🔙 Volver al menú"]
], resize_keyboard=True)

submenu_administrativo = ReplyKeyboardMarkup([
    ["Como descargar el recibo de la matricula"],
    ["Precuniarios"],
    ["Donde realizar la evaluación de profesores"],
    ["🔙 Volver al menú"]
], resize_keyboard=True)

submenu_plataformas = ReplyKeyboardMarkup([
    ["Aulas Virtuales"],
    ["Ubicacion de las sedes"],
    ["🔙 Volver al menú"]
], resize_keyboard=True)

submenu_contacto = ReplyKeyboardMarkup([
    ["Correos importantes"],
    ["🔙 Volver al menú"]
], resize_keyboard=True)

submenu_ingles = ReplyKeyboardMarkup([
    ["Curso de Inglés"],
    ["Examen de Inglés"],
    ["🔙 Volver al menú"]
], resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy el Asistente Mecatrónico 🤖\nSelecciona una categoría para comenzar:",
        reply_markup=teclado_categorias
    )

# Respuestas
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto == "🎓 Académico":
        await update.message.reply_text("Selecciona una opción académica:", reply_markup=submenu_academico)

    elif texto == "🏛️ Administrativo":
        await update.message.reply_text("Selecciona una opción administrativa:", reply_markup=submenu_administrativo)

    elif texto == "💻 Plataformas":
        await update.message.reply_text("Selecciona una opción de plataforma:", reply_markup=submenu_plataformas)

    elif texto == "📬 Contacto":
        await update.message.reply_text("Selecciona una opción de contacto:", reply_markup=submenu_contacto)

    elif texto == "Cursos y Exámenes de Inglés":
        await update.message.reply_text("¿Qué necesitas saber?", reply_markup=submenu_ingles)

    elif texto == "🔙 Volver al menú":
        await update.message.reply_text("🏠 Menú principal:", reply_markup=teclado_categorias)

    elif texto in FAQ:
        await update.message.reply_text(FAQ[texto], reply_markup=ReplyKeyboardMarkup([["🔙 Volver al menú"]], resize_keyboard=True))

    else:
        await update.message.reply_text("No entendí eso 😅. Usa el menú o escribe /start para comenzar.", reply_markup=teclado_categorias)

# Ejecutar bot
def main():
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = Application.builder().token("AQUI_TU_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("🤖 Bot en marcha...")
    app.run_polling()

if __name__ == '__main__':
    main()
