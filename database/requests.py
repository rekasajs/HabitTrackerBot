from sqlalchemy import select, update, delete

from database.models import async_session
from database.models import User, Habit, HabitCompletion

async def set_habit(user_id, name, frequency, reminder_time):
  async with async_session() as session:
    habit = await session.scalar(select(Habit).where(Habit.name == name))

    if not habit:
      session.add(Habit(user_id = user_id, name = name, frequency = frequency, reminder_time = reminder_time))
      await session.commit()

async def get_habits(user_id):
  async with async_session() as session:
    return await session.scalars(select(Habit).where(Habit.user_id == user_id))