from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
from pathlib import Path
import os

from agent import responder_mensagem

# Carrega .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_firstname = update.effective_user.first_name
    await update.message.reply_text(f"Salve, {user_firstname}! Bem-vindo ao mundo FURIOSO 🔥")

# Mensagens comuns
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_input = update.message.text
        await update.message.chat.send_action(action="typing")
        response_text = responder_mensagem(user_input)
        await update.message.reply_text(response_text)
    except Exception as e:
        print("Erro:", e)
        await update.message.reply_text("⚠️ Buguei aqui! Já já tô de volta na torcida 🛠️")

# Inicializa o bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("🔥 Bot está rodando... Ctrl+C para parar.")
    app.run_polling()

if __name__ == "__main__":
    main()