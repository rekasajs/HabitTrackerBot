from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.main_menu import main_menu

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Приветствую, {html.bold(message.from_user.full_name)}!", reply_markup=main_menu)

@router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer('Помощь по командам')