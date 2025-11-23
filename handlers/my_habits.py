import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.requests import get_habits, get_habit_by_id, delete_habit_by_id
from utils.changers import frequency_changer, is_active_changer
from keyboards.my_habit_options import my_habit_options

router = Router()

@router.message(F.text == '📊 Мои привычки')
async def command_my_habits_handler(message: Message) -> None:
    keyboard = InlineKeyboardBuilder()
    habits = await get_habits(message.from_user.id)
    for habit in habits:
      keyboard.add(InlineKeyboardButton(text = habit.name, callback_data=f'habit_{habit.id}'))
    await message.answer(f"📊 Список твоих привычек...", reply_markup=keyboard.adjust(2).as_markup())

@router.callback_query(F.data.startswith('habit_to_delete_'))
async def command_my_habit(callback: CallbackQuery) -> None:
   habit_id = callback.data.split('_')[-1]
   await callback.message.answer(await delete_habit_by_id(habit_id))
   await callback.answer()

@router.callback_query(F.data.startswith('habit_'))
async def command_my_habit(callback: CallbackQuery) -> None:
   habit_id = callback.data.split('_')[-1]
   habit = await get_habit_by_id(habit_id)
   await callback.message.answer(f"┌─ 📝 {habit.name}\n"
                                 f"├─ 📅 Периодичность: {frequency_changer(habit.frequency)}\n"
                                 f"├─ ⏰ Напоминание: {habit.reminder_time}\n"
                                 f"└─ {is_active_changer(habit.is_active)}", reply_markup=my_habit_options(habit.id))
   await callback.answer()