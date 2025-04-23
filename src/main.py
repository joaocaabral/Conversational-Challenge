from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_firstname = update.effective_user.first_name
    await update.message.reply_text(f"Salve, {user_firstname}! Bem-vindo ao mundo FURIOSO 🔥")

# Resposta a qualquer mensagem
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fala comigo, torcedor! Em breve vou te trazer stats da FURIA, curiosidades e memes 🦍")

# Inicializa o bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🔥 Bot está rodando... Ctrl+C para parar.")
    app.run_polling()

if __name__ == "__main__":
    main()
