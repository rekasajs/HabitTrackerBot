import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.requests import get_habits

router = Router()

@router.message(F.text == '📊 Мои привычки')
async def command_my_habits_handler(message: Message) -> None:
    keyboard = InlineKeyboardBuilder()
    habits = await get_habits(message.from_user.id)
    for habit in habits:
      keyboard.add(InlineKeyboardButton(text = habit.name, callback_data=f'habit_{habit.id}'))
    await message.answer(f"📊 Список твоих привычек...", reply_markup=keyboard.adjust(2).as_markup())