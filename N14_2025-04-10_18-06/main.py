from config import *
import logging
from datetime import datetime as dt

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> ReplyKeyboardMarkup:
    reply_keyboard = [
        ['/start', '/help'],
        ['/time', '/date'],
    ]
    return ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    markup = await keyboard(update, context)

    user = update.effective_user
    await update.message.reply_html(
        rf"Здравствуйте, {user.mention_html()}!",
        reply_markup=markup,
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Я получил сообщение {update.message.text}")

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Сейчас {dt.now().strftime('%H:%M:%S')}")

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Сегодня {dt.now().strftime('%d-%m-%y')}")


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("date", date))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
