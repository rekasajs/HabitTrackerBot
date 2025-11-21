from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, DateTime
from datetime import datetime

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase, AsyncAttrs): 
  pass

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  tg_id = Column(BigInteger, unique=True)
  name = Column(String(50))
  created_at = Column(DateTime, default=datetime.now)

  habits = relationship("Habit", back_populates="user")

class Habit(Base):
  __tablename__ = 'habits'

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  name = Column(String(125), unique=True)
  frequency = Column(String(20), nullable=False)
  reminder_time = Column(String(5), nullable=False)
  created_at = Column(DateTime, default=datetime.now)
  is_active = Column(Integer, default=True)

  user= relationship('User', back_populates="habits")
  completions = relationship("HabitCompletion", back_populates="habit")

class HabitCompletion(Base):
  __tablename__ = 'habit_completions'

  id = Column(Integer, primary_key=True, index=True)
  habit_id = Column(Integer, ForeignKey('habits.id'), nullable=False)
  is_completed = Column(Integer, default=1)
  created_at = Column(DateTime, default=datetime.now)

  habit = relationship("Habit", back_populates="completions")

async def async_main():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)