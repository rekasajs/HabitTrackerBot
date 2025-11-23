from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

def my_habit_options(habit_id):
  return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🗑️ Удалить', callback_data=f'habit_to_delete_{habit_id}')]])