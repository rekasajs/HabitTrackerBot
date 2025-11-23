import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.requests import get_habits, get_habit_by_id
from utils.changers import frequency_changer, is_active_changer
from keyboards.mood import mood_keyboard

router = Router()

@router.message(F.text == '😊 Отметить настроение')
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Какое у Вас настроение сегодня?", reply_markup=mood_keyboard)
