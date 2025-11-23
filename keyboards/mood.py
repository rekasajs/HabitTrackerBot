from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mood_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='😄', callback_data='mood_5'),
                                                       InlineKeyboardButton(text='🙂', callback_data='mood_4'),
                                                       InlineKeyboardButton(text='😐', callback_data='mood_3'),
                                                       InlineKeyboardButton(text='😔', callback_data='mood_2'),
                                                       InlineKeyboardButton(text='😢', callback_data='mood_1')]])