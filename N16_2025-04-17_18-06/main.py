import asyncio
import logging
import sys
from config import BOT_TOKEN

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

dp = Dispatcher()

reply_keyboard = [[KeyboardButton(text="1"), KeyboardButton(text="2")],
                  [KeyboardButton(text="3"), KeyboardButton(text="4")],
                  [KeyboardButton(text="5"), KeyboardButton(text="6")],]

markup = ReplyKeyboardMarkup(keyboard=reply_keyboard, one_time_keyboard=False, resize_keyboard=True)


@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Здравствуйте!", reply_markup=markup)

@dp.message(Command('stop'))
async def command_stop_handler(message: Message) -> None:
    await message.answer(f"До свидания. Клавиатура закрыта.", reply_markup=ReplyKeyboardRemove())


# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
