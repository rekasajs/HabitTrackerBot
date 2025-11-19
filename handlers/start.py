from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Приветствую, {html.bold(message.from_user.full_name)}!")

@router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer('Помощь по командам')

@router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")