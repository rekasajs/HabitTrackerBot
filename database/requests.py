from sqlalchemy import select, update, delete

from database.models import async_session
from database.models import User, Habit, HabitCompletion

async def user_start(user_tg_id, user_name):
  async with async_session() as session:
    user = await session.scalar(select(User).where(User.tg_id == user_tg_id))

    if not user:
      session.add(User(tg_id = user_tg_id, name = user_name))
      await session.commit()
      return f'Добро пожаловать, {user_name}'
    else:
      return f'С возвращением, {user_name}'

async def set_habit(user_id, name, frequency, reminder_time):
  async with async_session() as session:
    habit = await session.scalar(select(Habit).where(Habit.name == name))

    if not habit:
      session.add(Habit(user_id = user_id, name = name, frequency = frequency, reminder_time = reminder_time))
      await session.commit()

async def get_habits(user_id):
  async with async_session() as session:
   return  await session.scalars(select(Habit).where(Habit.user_id == user_id))
  
async def get_habit_by_id(habit_id):
  async with async_session() as session:
    return await session.scalar(select(Habit).where(Habit.id == habit_id))
  
async def delete_habit_by_id(habit_id):
  async with async_session() as session:
    result = await session.execute(delete(Habit).where(Habit.id == habit_id))
    await session.commit()
    if result.rowcount > 0:
        return '✅ Привычка успешно удалена'
    else:
        return '❌ Привычка не найдена'