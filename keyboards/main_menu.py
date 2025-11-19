from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='➕ Добавить привычку')],
                                          [KeyboardButton(text='📊 Мои привычки'), KeyboardButton(text='😊 Отметить настроение')], 
                                          [KeyboardButton(text='📈 Статистика'), KeyboardButton(text='⚙️ Настройки')]],
                                          resize_keyboard=True)