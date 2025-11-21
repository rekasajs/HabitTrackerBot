import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from keyboards.main_menu import main_menu
from database.requests import set_habit

router = Router()

class Habit(StatesGroup):
  name = State()
  frequency = State()
  reminder_time = State()

@router.message(F.text == '➕ Добавить привычку')
async def add_habit_handler(message: Message, state: FSMContext):
  await message.answer('Введите название привычки')
  await state.set_state(Habit.name)

@router.message(Habit.name)
async def add_habit_name(message: Message, state: FSMContext):
  await state.update_data(name = message.text)

  keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📅 Ежедневно", callback_data="daily")],
    [InlineKeyboardButton(text="📆 Еженедельно", callback_data="weekly")]
  ])

  await message.answer('Выберите переодичность привычки', reply_markup=keyboard)
  await state.set_state(Habit.frequency)

@router.callback_query(Habit.frequency)
async def add_habit_frequency(callback: CallbackQuery, state: FSMContext):
  await state.update_data(frequency = callback.data)

  await callback.message.answer('Введите время напоминания (например: 9:00)')
  await state.set_state(Habit.reminder_time)
  await callback.answer()

@router.message(Habit.reminder_time)
async def add_habit_reminder_time(message: Message, state: FSMContext):
  time_pattern = r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
    
  if not re.match(time_pattern, message.text):
    await message.answer(
        "❌ Неверный формат времени!\n"
        "Введите время в формате ЧЧ:MM (например: 09:30 или 14:00)\n"
    )
    return

  await state.update_data(reminder_time = message.text)
  data = await state.get_data()
  await set_habit(message.from_user.id, data['name'], data['frequency'], data['reminder_time'])
  await message.answer(
    f"✅ Привычка добавлена!\n\n"
    f"📝 Название: {data['name']}\n"
    f"📅 Периодичность: {frequency_changer(data['frequency'])}\n"
    f"⏰ Напоминание: {data['reminder_time']}",
    reply_markup=main_menu
  )

  await state.clear()

def frequency_changer(frequency):
  if frequency == 'daily':
    return 'Ежедневно'
  else:
    return 'Еженедельно'
