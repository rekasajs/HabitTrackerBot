from aiogram import Router, F
from aiogram.types import Message

router = Router()

# @router.message(F.text == '➕ Добавить привычку')
# async def add_habbit_handler(message: Message) -> None:
#     await message.answer(f"Введите название привычки, пожалуйста")

# @router.message(F.text == '📊 Мои привычки')
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"📊 Список твоих привычек...")

# @router.message(F.text == '😊 Отметить настроение')
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Какое у Вас настроение сегодня?")

@router.message(F.text == '📈 Статистика')
async def command_start_handler(message: Message) -> None:
    await message.answer(f"📈 Твоя статистика...")

@router.message(F.text == '⚙️ Настройки')
async def command_start_handler(message: Message) -> None:
    await message.answer(f"⚙️ Настройки...")
